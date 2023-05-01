from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.profiles.models import Profile
from .models import Rating


User = get_user_model()

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_agent_review(request, profile_id):
    agent_profile = Profile.objects.get(id=profile_id)
    data = request.data

    profile_user = User.objects.get(pkid=agent_profile.user.pkid)
    if profile_user == request.user.email:
        formatted_response = {"message":"You can't rate yourself"}
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

    alreadyExists = agent_profile.agent_review.filter(pkid=profile_user.pkid).exists()
    # agent_profile.agent_review.filter(pkid=profile_user.pkid).exists()


    if alreadyExists:
        formatted_response = {"detail":"Profile already reviewed"}
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)
    
    elif data["rating"] == 0:
        formatted_response = {"detail":"Please select a rating"}
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

    else:
        try:
            review = Rating.objects.create(
                rater = request.user,
                agent = agent_profile,
                rating = data['rating'],
                commet = data['comment'],
            )
            reviews = agent_profile.agent_review.all()
            agent_profile.num_reviews = len(reviews)

            total = 0
            for i in reviews:
                total += 1

            return Response("Review Added")
        except Exception as e:
            return Response({"Message":"User_id and Profile_id already exists. Pleasr try with different id's"})