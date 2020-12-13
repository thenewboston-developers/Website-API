# # -*- coding: utf-8 -*-
# from unittest.mock import ANY
#
# from freezegun import freeze_time
# from rest_framework import serializers, status
# from rest_framework.reverse import reverse
#
# from v1.users.factories.user import UserFactory
# from ..factories.team import TeamFactory
# from ..models.team import Team
#
#
# def test_teams_members_list(api_client, django_assert_max_num_queries):
#     teams = TeamFactory.create_batch(10, team_members=5)
#
#     with django_assert_max_num_queries(2):
#         r = api_client.get(reverse('team-list'))
#
#     assert r.status_code == status.HTTP_200_OK
#     assert len(r.data) == 10
#     assert r.data[0] == {
#         'pk': str(teams[0].pk),
#         'created_date': serializers.DateTimeField().to_representation(teams[0].created_date),
#         'modified_date': serializers.DateTimeField().to_representation(teams[0].modified_date),
#         'team_members_meta': [{
#             'user': user.user_id,
#             'is_lead': user.is_lead,
#             'pay_per_day': user.pay_per_day,
#             'job_title': user.job_title,
#             'created_date': serializers.DateTimeField().to_representation(user.created_date),
#             'modified_date': serializers.DateTimeField().to_representation(user.modified_date),
#         } for user in teams[0].team_members.order_by('created_date').all()],
#         'title': teams[0].title,
#     }
#
#
# def test_teams_members_members_empty_post(api_client, staff_user):
#     api_client.force_authenticate(staff_user)
#
#     with freeze_time() as frozen_time:
#         r = api_client.post(reverse('team-list'), data={
#             'title': 'Star team',
#         }, format='json')
#
#     assert r.status_code == status.HTTP_201_CREATED
#     assert r.data == {
#         'pk': ANY,
#         'created_date': serializers.DateTimeField().to_representation(frozen_time()),
#         'modified_date': serializers.DateTimeField().to_representation(frozen_time()),
#         'team_members_meta': [],
#         'title': 'Star team',
#     }
#     assert Team.objects.get(pk=r.data['pk']).title == 'Star team'
#
#
# def test_teams_members_post(api_client, staff_user):
#     api_client.force_authenticate(staff_user)
#
#     users = UserFactory.create_batch(5)
#
#     with freeze_time() as frozen_time:
#         r = api_client.post(reverse('team-list'), data={
#             'title': 'Star team',
#             'team_members_meta': [
#                 {
#                     'user': users[1].pk,
#                     'is_lead': True,
#                     'pay_per_day': 19001,
#                     'job_title': 'Back-End Developer'
#                 },
#                 {
#                     'user': users[3].pk,
#                     'is_lead': False,
#                     'pay_per_day': 9001,
#                     'job_title': 'Front-End Developer'
#                 }
#             ],
#         }, format='json')
#
#     assert r.status_code == status.HTTP_201_CREATED
#     assert r.data == {
#         'pk': ANY,
#         'created_date': serializers.DateTimeField().to_representation(frozen_time()),
#         'modified_date': serializers.DateTimeField().to_representation(frozen_time()),
#         'team_members_meta': [
#             {
#                 'created_date': serializers.DateTimeField().to_representation(frozen_time()),
#                 'modified_date': serializers.DateTimeField().to_representation(frozen_time()),
#                 'user': users[1].pk,
#                 'is_lead': True,
#                 'pay_per_day': 19001,
#                 'job_title': 'Back-End Developer'
#             },
#             {
#                 'created_date': serializers.DateTimeField().to_representation(frozen_time()),
#                 'modified_date': serializers.DateTimeField().to_representation(frozen_time()),
#                 'user': users[3].pk,
#                 'is_lead': False,
#                 'pay_per_day': 9001,
#                 'job_title': 'Front-End Developer'
#             }
#         ],
#         'title': 'Star team',
#     }
#     assert Team.objects.get(pk=r.data['pk']).title == 'Star team'
#
#
# def test_teams_members_patch(api_client, staff_user):
#     api_client.force_authenticate(staff_user)
#
#     user = UserFactory()
#     team = TeamFactory(team_members=2)
#
#     with freeze_time() as frozen_time:
#         r = api_client.patch(
#             reverse('team-detail', (team.pk,)),
#             data={
#                 'title': 'Star team',
#                 'team_members_meta': [
#                     {
#                         'user': team.team_members.all()[1].user_id,
#                         'is_lead': True,
#                         'pay_per_day': 19001,
#                         'job_title': 'Back-End Developer'
#                     },
#                     {
#                         'user': user.pk,
#                         'is_lead': False,
#                         'pay_per_day': 9001,
#                         'job_title': 'Front-End Developer'
#                     }
#                 ]
#             },
#             format='json'
#         )
#
#     assert r.status_code == status.HTTP_200_OK
#     assert r.data == {
#         'pk': str(team.pk),
#         'created_date': serializers.DateTimeField().to_representation(team.created_date),
#         'modified_date': serializers.DateTimeField().to_representation(frozen_time()),
#         'team_members_meta': [
#             {
#                 'created_date': serializers.DateTimeField().to_representation(frozen_time()),
#                 'modified_date': serializers.DateTimeField().to_representation(frozen_time()),
#                 'user': user.pk,
#                 'is_lead': False,
#                 'pay_per_day': 9001,
#                 'job_title': 'Front-End Developer'
#             },
#             {
#                 'created_date': serializers.DateTimeField().to_representation(
#                     team.team_members.all()[1].created_date
#                 ),
#                 'modified_date': serializers.DateTimeField().to_representation(frozen_time()),
#                 'user': team.team_members.all()[1].user_id,
#                 'is_lead': True,
#                 'pay_per_day': 19001,
#                 'job_title': 'Back-End Developer'
#             },
#         ],
#         'title': 'Star team',
#     }
#
#     assert Team.objects.get(pk=str(team.pk)).title == 'Star team'
#
#
# def test_teams_members_delete(api_client, staff_user):
#     api_client.force_authenticate(staff_user)
#
#     team = TeamFactory(team_members=2)
#
#     r = api_client.delete(reverse('team-detail', (team.pk,)))
#
#     assert r.status_code == status.HTTP_204_NO_CONTENT
#     assert r.data is None
#
#     assert Team.objects.filter(pk=str(team.pk)).first() is None
#
#
# def test_opening_anon_post(api_client):
#     r = api_client.post(reverse('team-list'), data={'title': 'sometitle'}, format='json')
#
#     assert r.status_code == status.HTTP_401_UNAUTHORIZED
#
#
# def test_teams_members_anon_patch(api_client):
#     team = TeamFactory()
#
#     r = api_client.post(reverse('team-detail', (team.pk,)), data={'title': 'sometitle'}, format='json')
#
#     assert r.status_code == status.HTTP_401_UNAUTHORIZED
#
#
# def test_teams_members_anon_delete(api_client):
#     team = TeamFactory()
#
#     r = api_client.delete(reverse('team-detail', (team.pk,)))
#
#     assert r.status_code == status.HTTP_401_UNAUTHORIZED