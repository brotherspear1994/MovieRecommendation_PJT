from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
    # Client 에서 보내온 정보 받기
    password = request.data.get('password')
    passwordConfirmation = request.data.get('passwordConfirmation')
    # 비밀번호 일치 여부 확인
    if password != passwordConfirmation:
        return Response({ 'error': '비밀번호가 일치하지 않습니다.'})

    # 사용자가 보낸 데이터로 UserSerializer 를 통해 데이터 생성
    else:
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # 그냥 저장하고 끝내면 비밀번호 유출
            user = serializer.save()

            # 비밀번호 해싱
            user.set_password(request.data.get('password'))
            user.save()

            return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_profile(request):

    user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    serializer = UserSerializer(user)

    return Response(serializer.data)



@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request, username):
    # print(request.data)
    user = get_object_or_404(get_user_model(), pk=request.data.get('user_pk'))
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def users(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def follow(request, my_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    me = get_object_or_404(get_user_model(), pk=my_pk)
    if person != me:
        if me.followings.filter(pk=person.pk).exists():
        # if user in person.followers.all():
            me.followings.remove(person)
            following = False
            # followed가 더 좋은 표현인 듯
        else:
            me.followings.add(person)
            following = True
        print(me.followings.filter(pk=person.pk))
        return Response(following)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def users_info(request):
    # print(request.data)
    users = request.data.get('users')
    movies = []
    for user in users:
        user = get_object_or_404(get_user_model(), pk=user)
        serializer = UserSerializer(user)
        # print(serializer.data)
        like_movies = serializer.data.get('like_movies')
        for movie in like_movies:
            if movie not in movies:
                movies.append(movie)
    
    return Response(movies)
