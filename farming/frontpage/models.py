# # -*- coding: utf-8 -*-
# # -*- from __future__ import unicode_literals
#
# from django.db import models
#
# class Album(models.Model):
#     artist=models.CharField(max_length=52)
#     album_title=models.CharField(max_length=522)
#     genre = models.CharField(max_length=522)
#
#
# class Song(models.Model):
#     album = models.ForeignKey(Album, on_delete=models.CASCADE)
#     file_type=models.CharField(max_length=10)
#     song_title=models.CharField(max_length=100)
