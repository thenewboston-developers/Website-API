import factory
from django.utils import timezone
from factory.django import DjangoModelFactory

from ..models.category import Category
from ..models.playlist import Playlist
from ..models.video import Video


class PlaylistFactory(DjangoModelFactory):
    playlist_id = factory.Faker('pystr', max_chars=50)
    title = factory.Faker('pystr', max_chars=250)
    description = factory.Faker('text')
    published_at = factory.Faker('date_time', tzinfo=timezone.get_current_timezone())
    author = factory.Faker('pystr', max_chars=250)
    thumbnail = factory.Faker('pystr', max_chars=250)
    language = factory.Faker('pystr', max_chars=250)
    playlist_type = factory.Faker('pystr', max_chars=11)

    class Meta:
        model = Playlist

    @factory.post_generation
    def videos(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            if isinstance(extracted, int):
                VideoFactory.create_batch(extracted, playlist=self)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            if not isinstance(extracted, (int, list, set, tuple)):
                return
            if isinstance(extracted, int):
                for _ in range(extracted):
                    self.categories.add(CategoryFactory())
            else:
                for category in extracted:
                    self.categories.add(category)


class VideoFactory(DjangoModelFactory):
    video_id = factory.Faker('pystr', max_chars=11)
    title = factory.Faker('pystr', max_chars=250)
    description = factory.Faker('text')
    published_at = factory.Faker('date_time', tzinfo=timezone.get_current_timezone())
    duration = factory.Faker('pyint')
    author = factory.Faker('pystr', max_chars=250)
    tags = factory.Faker('pylist', nb_elements=10, variable_nb_elements=True, value_types='str')
    thumbnail = factory.Faker('pystr', max_chars=250)
    language = factory.Faker('pystr', max_chars=250)
    video_type = factory.Faker('pystr', max_chars=11)
    playlist = factory.SubFactory(PlaylistFactory)

    class Meta:
        model = Video

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            if not isinstance(extracted, (int, list, set, tuple)):
                return
            if isinstance(extracted, int):
                for _ in range(extracted):
                    self.categories.add(CategoryFactory())
            else:
                for category in extracted:
                    self.categories.add(category)


class CategoryFactory(DjangoModelFactory):
    name = factory.Faker('pystr', max_chars=250)

    class Meta:
        model = Category
