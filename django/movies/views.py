from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status

from .models import Movie, Community, Comment, Review, ReviewComment, Genre
from .serializers import MovieSerializer, CommunityListSerializer, CommentSerializer, ReviewListSerializer, ReviewCommentSerializer


@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_list_create(request):
  if request.method == 'GET':
    communities = Community.objects.all()
    serializer = CommunityListSerializer(communities, many=True)
    return Response(serializer.data)
  else:
    serializer = CommunityListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_detail(request, community_pk):
  community = get_object_or_404(Community, pk=community_pk)

  serializer = CommunityListSerializer(community)
  return Response(serializer.data)
    

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    comments = community.comment_set.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_comment(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):

        serializer.save(user=request.user, community=community)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(comment.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_update_delete(request, community_pk):
  community = get_object_or_404(Community, pk=community_pk)

  if not request.user.communities.filter(pk=community_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  if request.method == 'PUT':
      serializer = CommunityListSerializer(community, data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user)
          return Response(serializer.data)
  else:
      community.delete()
      return Response({ 'id': community_pk })


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, community_pk, comment_pk):
  community = get_object_or_404(Community, pk=community_pk)
  comment = community.comment_set.get(pk=comment_pk)

  if not request.user.comments.filter(pk=comment_pk).exists():
    return Response({'message': '권한이 없습니다.'})
  else:
    comment.delete()
    return Response({ 'id': comment_pk })
  
  
### review

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_create(request, movie_pk):
  if request.method == 'GET':
    reviews = Review.objects.all().filter(movie_id=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
  else:
    serializer = ReviewListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      movie = get_object_or_404(Movie, pk=request.data.get('movie'))

      pre_point = movie.vote_average * movie.vote_count
      pre_count = movie.vote_count

      point = pre_point+request.data.get('rank')
      count = movie.vote_count + 1
      new_vote_average = round(point/count, 2)

      movie.vote_average = new_vote_average
      movie.vote_count = count
      movie.save()
        
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_comment_list(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  comments = review.reviewcomment_set.all()
  serializer = ReviewCommentSerializer(comments, many=True)
  return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review_comment(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  serializer = ReviewCommentSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save(user=request.user, review=review)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  if not request.user.reviews.filter(pk=review_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  if request.method == 'PUT':
    serializer = ReviewListSerializer(review, data=request.data)
    
    if serializer.is_valid(raise_exception=True):
      movie = get_object_or_404(Movie, pk=request.data.get('movie'))
      pre_point = movie.vote_average * (movie.vote_count - 1)
      pre_count = movie.vote_count - 1
      point = pre_point+request.data.get('rank')
      count = movie.vote_count
      new_vote_average = round(point/count, 2)
      movie.vote_average = new_vote_average
      movie.vote_count = count
      movie.save()
      serializer.save(user=request.user)
      return Response(serializer.data)

  else:
    review = get_object_or_404(Review, pk=review_pk)
    movie = get_object_or_404(Movie, pk=review.movie_id)
    pre_point = movie.vote_average * (movie.vote_count)
    pre_count = movie.vote_count
    point = pre_point - review.rank
    count = movie.vote_count-1
    new_vote_average = round(point/count, 2)
    movie.vote_average = new_vote_average
    movie.vote_count = count
    movie.save()
    review.delete()
    return Response({ 'id': review_pk })


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_comment_delete(request, review_pk, review_comment_pk):
  review = get_object_or_404(Review, pk=review_pk)
  comment = review.reviewcomment_set.get(pk=review_comment_pk)
  if not request.user.review_comments.filter(pk=review_comment_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  else:
    comment.delete()
    return Response({ 'id': review_comment_pk })


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend(request):
  favorite_movies = Movie.objects.all().order_by('-vote_average')[:30]
  serializer1 = MovieSerializer(favorite_movies, many=True)
  shortest_movies = Movie.objects.all().order_by('runtime')[30:60]
  serializer2 = MovieSerializer(shortest_movies, many=True)
  # 리뷰 기반 장르 추천
  users_movies = []
  # 좋아요 기반
  users_movies2 = []
  reviews = Review.objects.all()
  for review in reviews:
    movie = Movie.objects.get(pk=review.movie_id)
    if not movie in users_movies:
      users_movies.append(movie)

  if users_movies:
    serializer = MovieSerializer(users_movies[0])
    genre = serializer.data.get('genres')[0]
    genre_name = Genre.objects.get(id=genre)
    idx = 1
    while len(users_movies) < 30:
      movie = Movie.objects.get(pk=idx)
      ser = MovieSerializer(movie)
      if ser.data.get('genres')[0] == genre and movie not in users_movies:
        users_movies.append(movie)
      idx += 1
      if idx == 979:
        users_movies = Movie.objects.all().order_by('release_date')[:30]
  
  else:
    users_movies = Movie.objects.all().order_by('release_date')[:30]

  like_movies = request.data.get('like_movies')
  for like_movie in like_movies:
    movie = get_object_or_404(Movie, pk=like_movie)
    if not movie in users_movies2:
      users_movies2.append(movie)

  serializer3 = MovieSerializer(users_movies, many=True)
  serializer4 = MovieSerializer(users_movies2, many=True) 
  
  return Response([serializer1.data, serializer2.data, serializer3.data, serializer4.data])


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_like(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      liking = False
      
  else:
      me.like_movies.add(movie.pk)
      liking = True
  
  return Response(liking)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_movie_like(request, my_pk):
  me = get_object_or_404(get_user_model(), pk=my_pk)
  data = []
  movies = request.data
  for movie_pk in movies:
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    data.append(serializer.data)
  
  return Response(data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_movie_users(request, my_pk):
  # print(request.data)
  users = []
  movies = request.data.get('movies')
  # print(movies)
  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie)
    serializer = MovieSerializer(movie)
    # print(serializer.data)
    for user in serializer.data.get('like_users'):
      if user not in users:
        users.append(user)

  return Response(users)
