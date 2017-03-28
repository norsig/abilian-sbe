# coding=utf-8
"""
Forum views
"""

from flask_login import current_user
from flask import current_app, g
from abilian.services.activitytracker import activitytracker


def object_viewers(current_object):
    if current_user.has_role('manager'):
            tracked_viewers = activitytracker.get_viewers(current_object.id)
            viewers_id = [user.user_id for user in tracked_viewers]
            viewers = filter(lambda user: user.id in list(viewers_id) and user.id != current_object.creator.id, g.community.members)
            return viewers
