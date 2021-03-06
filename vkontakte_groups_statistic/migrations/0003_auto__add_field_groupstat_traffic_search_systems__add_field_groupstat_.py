# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'GroupStat.traffic_search_systems'
        db.add_column('vkontakte_groups_groupstat', 'traffic_search_systems',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'GroupStat.traffic_external_sites'
        db.add_column('vkontakte_groups_groupstat', 'traffic_external_sites',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'GroupStat.traffic_my_groups'
        db.add_column('vkontakte_groups_groupstat', 'traffic_my_groups',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'GroupStat.traffic_news'
        db.add_column('vkontakte_groups_groupstat', 'traffic_news',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'GroupStat.traffic_top'
        db.add_column('vkontakte_groups_groupstat', 'traffic_top',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'GroupStat.traffic_search_results'
        db.add_column('vkontakte_groups_groupstat', 'traffic_search_results',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'GroupStat.traffic_users'
        db.add_column('vkontakte_groups_groupstat', 'traffic_users',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'GroupStat.traffic_groups'
        db.add_column('vkontakte_groups_groupstat', 'traffic_groups',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'GroupStat.traffic_applications'
        db.add_column('vkontakte_groups_groupstat', 'traffic_applications',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'GroupStat.traffic_bookmarklets'
        db.add_column('vkontakte_groups_groupstat', 'traffic_bookmarklets',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'GroupStat.traffic_search_systems'
        db.delete_column('vkontakte_groups_groupstat', 'traffic_search_systems')

        # Deleting field 'GroupStat.traffic_external_sites'
        db.delete_column('vkontakte_groups_groupstat', 'traffic_external_sites')

        # Deleting field 'GroupStat.traffic_my_groups'
        db.delete_column('vkontakte_groups_groupstat', 'traffic_my_groups')

        # Deleting field 'GroupStat.traffic_news'
        db.delete_column('vkontakte_groups_groupstat', 'traffic_news')

        # Deleting field 'GroupStat.traffic_top'
        db.delete_column('vkontakte_groups_groupstat', 'traffic_top')

        # Deleting field 'GroupStat.traffic_search_results'
        db.delete_column('vkontakte_groups_groupstat', 'traffic_search_results')

        # Deleting field 'GroupStat.traffic_users'
        db.delete_column('vkontakte_groups_groupstat', 'traffic_users')

        # Deleting field 'GroupStat.traffic_groups'
        db.delete_column('vkontakte_groups_groupstat', 'traffic_groups')

        # Deleting field 'GroupStat.traffic_applications'
        db.delete_column('vkontakte_groups_groupstat', 'traffic_applications')

        # Deleting field 'GroupStat.traffic_bookmarklets'
        db.delete_column('vkontakte_groups_groupstat', 'traffic_bookmarklets')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'vkontakte_groups.group': {
            'Meta': {'ordering': "['name']", 'object_name': 'Group'},
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'photo_big': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'photo_medium': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'remote_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['vkontakte_users.User']", 'symmetrical': 'False'})
        },
        'vkontakte_groups_statistic.groupstat': {
            'Meta': {'ordering': "('group', 'date')", 'unique_together': "(('group', 'date'),)", 'object_name': 'GroupStat', 'db_table': "'vkontakte_groups_groupstat'"},
            'act_members': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'act_visitors': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'activity_photo_comments': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'activity_photos': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'activity_topic_comments': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'activity_topics': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'activity_video_comments': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'activity_videos': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'activity_wall': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'ads_members': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'ads_visitors': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_18': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_18_21': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_21_24': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_24_27': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_27_30': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_30_35': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_35_45': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_45': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'comments': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'ex_members': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'females': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statistics'", 'to': "orm['vkontakte_groups.Group']"}),
            'hidings': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'males': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'members': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'new_members': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reach': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reach_age_18': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reach_age_18_21': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reach_age_21_24': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reach_age_24_27': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reach_age_27_30': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reach_age_30_35': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reach_age_35_45': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reach_age_45': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reach_females': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reach_males': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reach_subsribers': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'references': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'section_applications': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'section_audio': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'section_discussions': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'section_documents': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'section_photoalbums': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'section_video': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'shares': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'traffic_applications': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'traffic_bookmarklets': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'traffic_external_sites': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'traffic_groups': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'traffic_my_groups': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'traffic_news': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'traffic_search_results': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'traffic_search_systems': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'traffic_top': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'traffic_users': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'visitors': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'widget_ex_users': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'widget_members_views': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'widget_new_users': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'widget_users_views': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'})
        },
        'vkontakte_groups_statistic.groupstatistic': {
            'Meta': {'ordering': "('group', 'date')", 'unique_together': "(('group', 'date'),)", 'object_name': 'GroupStatistic', 'db_table': "'vkontakte_groups_groupstatistic'"},
            'age_18': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_18_21': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_21_24': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_24_27': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_27_30': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_30_35': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_35_45': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_45': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'females': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statistics_api'", 'to': "orm['vkontakte_groups.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'males': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'visitors': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'})
        },
        'vkontakte_groups_statistic.groupstatpercentage': {
            'Meta': {'ordering': "('group', '-type', 'order')", 'unique_together': "(('group', 'type', 'value_type'),)", 'object_name': 'GroupStatPercentage', 'db_table': "'vkontakte_groups_groupstatpercentage'"},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'percentage_statistics'", 'to': "orm['vkontakte_groups.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'percents': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'value': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'value_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'value_type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'vkontakte_places.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cities'", 'null': 'True', 'to': "orm['vkontakte_places.Country']"}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'remote_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'})
        },
        'vkontakte_places.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'remote_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'})
        },
        'vkontakte_users.user': {
            'Meta': {'ordering': "['remote_id']", 'object_name': 'User'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'activity': ('django.db.models.fields.TextField', [], {}),
            'albums': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'audios': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bdate': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'books': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vkontakte_places.City']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'counters_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vkontakte_places.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'facebook_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'faculty': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'faculty_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'followers': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'friends': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'friends_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'friends_users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'followers_users'", 'symmetrical': 'False', 'to': "orm['vkontakte_users.User']"}),
            'games': ('django.db.models.fields.TextField', [], {}),
            'graduation': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'has_mobile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.TextField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'livejournal': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'movies': ('django.db.models.fields.TextField', [], {}),
            'mutual_friends': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'notes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'photo_big': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'photo_medium': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'photo_medium_rec': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'photo_rec': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'rate': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'relation': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            'remote_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'subscriptions': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'sum_counters': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'timezone': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tv': ('django.db.models.fields.TextField', [], {}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'university': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'university_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'user_photos': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user_videos': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'videos': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'wall_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'vkontakte_wall.comment': {
            'Meta': {'ordering': "['post', '-date']", 'object_name': 'Comment'},
            'author_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': "orm['contenttypes.ContentType']"}),
            'author_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'from_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wall_comments'", 'to': "orm['vkontakte_wall.Post']"}),
            'raw_html': ('django.db.models.fields.TextField', [], {}),
            'remote_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'20'"}),
            'reply_for_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'replies'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'reply_for_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'reply_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vkontakte_wall.Comment']", 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'wall_owner_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vkontakte_wall_comments'", 'to': "orm['contenttypes.ContentType']"}),
            'wall_owner_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'vkontakte_wall.post': {
            'Meta': {'ordering': "['wall_owner_id', '-date']", 'object_name': 'Post'},
            'attachments': ('django.db.models.fields.TextField', [], {}),
            'author_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vkontakte_posts'", 'to': "orm['contenttypes.ContentType']"}),
            'author_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'comments': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'copy_owner_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vkontakte_wall_copy_posts'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'copy_owner_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'copy_post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vkontakte_wall.Post']", 'null': 'True'}),
            'copy_text': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'geo': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like_users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'like_posts'", 'blank': 'True', 'to': "orm['vkontakte_users.User']"}),
            'likes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'media': ('django.db.models.fields.TextField', [], {}),
            'online': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'post_source': ('django.db.models.fields.TextField', [], {}),
            'raw_html': ('django.db.models.fields.TextField', [], {}),
            'remote_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'20'"}),
            'reply_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'repost_users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'repost_posts'", 'blank': 'True', 'to': "orm['vkontakte_users.User']"}),
            'reposts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'signer_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'wall_owner_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vkontakte_wall_posts'", 'to': "orm['contenttypes.ContentType']"}),
            'wall_owner_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['vkontakte_groups_statistic']