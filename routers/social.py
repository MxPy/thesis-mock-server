from fastapi import Depends, status, HTTPException, APIRouter, Body, Request
from fastapi.responses import Response
import schemas



router = APIRouter(
    prefix='/social',
    tags=['social'])

feedpost = {
    "post_id": 0, #db key
    "feed_post_body":{
        "subforum_id": 0, #int
        "subforum_name": "", #string
        "creator_id": 0, #uuid4
        "creator_nickname": "", #string
        "title": "", #string
        "shortened_body": "",#string Optional, not exist if image exist, max 40 words
        "image": "image_link_etc", #link to image stroed in other service, Optional, not exist if shortened_body exist
        "vote_count": 0 #int
    }
}

feed = [
    {
        "post_id": 1,
        "feed_post_body": {
            "subforum_id": 101,
            "subforum_name": "Running",
            "creator_id": 7,
            "creator_nickname": "FastRunner",
            "title": "My First Marathon Experience",
            "shortened_body": "Running my first marathon was a life-changing experience. The thrill of crossing the finish line...",
            "vote_count": 132
        }
    },
    {
        "post_id": 2,
        "feed_post_body": {
            "subforum_id": 102,
            "subforum_name": "Fitness",
            "creator_id": 43,
            "creator_nickname": "GymGuru",
            "title": "Top 5 Strength Training Tips",
            "shortened_body": "Strength training is essential for building muscle and staying healthy. Here are my top 5 tips to...",
            "vote_count": 97
        }
    },
    {
        "post_id": 3,
        "feed_post_body": {
            "subforum_id": 101,
            "subforum_name": "Running",
            "creator_id": 34,
            "creator_nickname": "TrailBlazer",
            "title": "The Beauty of Trail Running",
            "shortened_body": "Trail running offers an escape into nature and a break from the monotony of road running...",
            "vote_count": 54
        }
    },
    {
        "post_id": 4,
        "feed_post_body": {
            "subforum_id": 103,
            "subforum_name": "Nutrition",
            "creator_id": 22,
            "creator_nickname": "FitFoodie",
            "title": "Best Pre-Workout Meals",
            "image": "https://example.com/preworkoutmeals.jpg",
            "vote_count": 78
        }
    },
    {
        "post_id": 5,
        "feed_post_body": {
            "subforum_id": 102,
            "subforum_name": "Fitness",
            "creator_id": 14,
            "creator_nickname": "FlexMaster",
            "title": "How to Improve Your Squat",
            "image": "https://example.com/improveyoursquat.jpg",
            "vote_count": 105
        }
    },
    {
        "post_id": 6,
        "feed_post_body": {
            "subforum_id": 101,
            "subforum_name": "Running",
            "creator_id": 69,
            "creator_nickname": "Speedster",
            "title": "Interval Training for Speed",
            "shortened_body": "If you're looking to improve your running speed, interval training is a must...",
            "vote_count": 88
        }
    },
    {
        "post_id": 7,
        "feed_post_body": {
            "subforum_id": 103,
            "subforum_name": "Nutrition",
            "creator_id": 420,
            "creator_nickname": "HealthNut",
            "title": "Hydration Tips for Runners",
            "shortened_body": "Staying hydrated is crucial for runners, especially during long distances...",
            "vote_count": 66
        }
    },
    {
        "post_id": 8,
        "feed_post_body": {
            "subforum_id": 102,
            "subforum_name": "Fitness",
            "creator_id": 6969,
            "creator_nickname": "BeastMode",
            "title": "HIIT Workouts You Can Do at Home",
            "image": "https://example.com/hiitworkout.jpg",
            "vote_count": 112
        }
    },
    {
        "post_id": 9,
        "feed_post_body": {
            "subforum_id": 101,
            "subforum_name": "Running",
            "creator_id": 469,
            "creator_nickname": "RunMachine",
            "title": "The Best Running Shoes for Beginners",
            "shortened_body": "Choosing the right pair of running shoes is essential for beginners to prevent injuries and enhance performance...",
            "vote_count": 74
        }
    },
    {
        "post_id": 10,
        "feed_post_body": {
            "subforum_id": 102,
            "subforum_name": "Fitness",
            "creator_id": 69420,
            "creator_nickname": "FitFanatic",
            "title": "Full-Body Workouts Without Weights",
            "image": "https://example.com/fullbodyworkout.jpg",
            "vote_count": 83
        }
    },
    {
        "post_id": 11,
        "feed_post_body": {
            "subforum_id": 103,
            "subforum_name": "Nutrition",
            "creator_id": 80085,
            "creator_nickname": "MacroMaster",
            "title": "Understanding Macronutrients",
            "shortened_body": "Macronutrients are the building blocks of a healthy diet. Here's a simple guide to understanding them...",
            "vote_count": 92
        }
    },
    {
        "post_id": 12,
        "feed_post_body": {
            "subforum_id": 101,
            "subforum_name": "Running",
            "creator_id": 102,
            "creator_nickname": "SprintKing",
            "title": "The Mental Game of Running",
            "shortened_body": "Running is as much a mental challenge as it is a physical one. Here's how to stay strong...",
            "vote_count": 69
        },
    },

    {
        "post_id": 13,
        "feed_post_body": {
            "subforum_id": 102,
            "subforum_name": "Fitness",
            "creator_id": 14,
            "creator_nickname": "FlexMaster",
            "title": "How to Improve Your Squat",
            "image": "https://example.com/improveyoursquat.jpg",
            "vote_count": 105
        }
    },
    {
        "post_id": 14,
        "feed_post_body": {
            "subforum_id": 101,
            "subforum_name": "Running",
            "creator_id": 69,
            "creator_nickname": "Speedster",
            "title": "Interval Training for Speed",
            "shortened_body": "If you're looking to improve your running speed, interval training is a must...",
            "vote_count": 88
        }
    },
    {
        "post_id": 15,
        "feed_post_body": {
            "subforum_id": 103,
            "subforum_name": "Nutrition",
            "creator_id": 420,
            "creator_nickname": "HealthNut",
            "title": "Hydration Tips for Runners",
            "shortened_body": "Staying hydrated is crucial for runners, especially during long distances...",
            "vote_count": 66
        }
    },
]


@router.get("/post/{post_id}")
def health_check(post_id: int):
    return feedpost

@router.get("/feed")
def health_check():
    return feed