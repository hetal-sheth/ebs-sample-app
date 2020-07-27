from flask import Flask
# from flask import Blueprint
# from yrb_swagger import youngRB_blueprint
# from validate_coupon import coupon
# from downloads_service import analysis
# from user_tracking_service import user_tracking
# from board_and_class_registrations import myelsa_registrations
# from wotd_service import wotd_notification
# from onboard_teacher import onboarding_teachers
# from played_daily_contest_notification_service import daily_contest_notification
# from daily_notifications import daily_notifications
# from reading_service import reading_service
# from YNGrbContest import yrb_notification
# from text_to_speech import text_to_speech
# from user_product_time_dis import time_discount
from activity import student_favorite
# from elsa_avatar import avatar
# from avatar_polls import avatar_polls
# from grammar_contentdetails import grammar_content_details
# from comm_admin_portal import comm_admin_portal
# from speech_to_text_service import speech_to_text
# from student_mock_test import mock_test
# from change_mock_test import mock_ques
# from coupon_validation import coupon_validation
# from insert_coins import insert_coins
# from contentwise_progress import contentwise_progress
# from product_rating import product_rating
# from string_to_audio import string_to_audio
# from currriculum_preview_portal import cur_pre_portal
# from parents_section import parents_service
# from report_analysis import report_analysis
# from admin_section import admin_section
# from job_portal import job_portal
# from myelsa_spellbee import spellbee
# from jobportal_otp import otp_jobportal
# from myelsa_mail_and_sms import myelsa_sms_mail
# from yrb_admin_portal import yrb_admin_portal
# from myelsa_registration_api import myelsa_registration
# from teacher_portal import teacher_portal
# from marks_remarks_on_mocktest import marks_n_remarks
# from subscription_from_sales_app import sales_app_subcription
# from chatbot import chatbot
# from fee_management import fee_management
# from logindb_services import logindb_controller
# from bookfair_section import games_section
# from myCommunication_section import mycomm_controller
# from student_subscription import student_subscription
# from cash_transactions import cash_transaction
# from user_library import user_library
# from zoom_videocall import live_classes
# from user_assessments import user_library_assessments
# from add_teacher_to_institution import teacher_to_institution
# from aws_resources import aws_resources
# from engagement_portal import engagement_portal
# from push_notifications import myelsa_app_notify
# from voicechat_section import voicechat_section
# from demo_onboarding import demo_onboarding
# from mylibrary import my_Library
# from onlinetest_section import onlinetest_section
# from instamojo_payments import instamojo_payments
# from create_institution_for_teacher import create_institute_for_teacher
# from myelsa_course import myelsa_course
# from userlibrary_dtls import library
# from online_test import online_test
# from course_section import course_section


application = Flask(__name__)
# application.config['SERVER_NAME'] = "127.0.0.1:8081"
# application.register_blueprint(course_section, url_prefix='/course_section')
# application.register_blueprint(online_test, url_prefix='/online_test')
# application.register_blueprint(library, url_prefix='/library_dtls')
# application.register_blueprint(myelsa_course, url_prefix='/myelsa_course')
# application.register_blueprint(create_institute_for_teacher, url_prefix='/create_institute')
# application.register_blueprint(instamojo_payments, url_prefix='/instamojo_payments')
# application.register_blueprint(onlinetest_section,url_prefix='/onlinetest_section')
# application.register_blueprint(my_Library,url_prefix='/my_Library')
# application.register_blueprint(demo_onboarding,url_prefix='/demo_onboarding_data')
# application.register_blueprint(voicechat_section,url_prefix='/voicechat_section')
# application.register_blueprint(myelsa_app_notify,url_prefix='/app_notify')
# application.register_blueprint(aws_resources,url_prefix='/aws_portal')
# application.register_blueprint(youngRB_blueprint,url_prefix='/yrb')
# application.register_blueprint(coupon,url_prefix='/coupon')
# application.register_blueprint(analysis,url_prefix='/myelsa_analysis')
# application.register_blueprint(user_tracking,url_prefix='/user_tracking')
# application.register_blueprint(myelsa_registrations,url_prefix='/myelsa_registrations')
# # application.register_blueprint(wotd_notification,url_prefix='/wotd_notification')
# application.register_blueprint(onboarding_teachers,url_prefix='/onboarding_teachers')
# # application.register_blueprint(daily_contest_notification,url_prefix = '/daily_contest_notification')
# # application.register_blueprint(summaryAndTrending,url_prefix = '/summaryAndTrending')
# application.register_blueprint(daily_notifications,url_prefix='/daily_notifications')
# application.register_blueprint(reading_service,url_prefix='/matchReadingAnswer')
# application.register_blueprint(yrb_notification,url_prefix='/YngRbContestNotification')
# application.register_blueprint(text_to_speech, url_prefix='/angrezdost')
# application.register_blueprint(time_discount, url_prefix='/time_discount')
application.register_blueprint(student_favorite, url_prefix='/favoriteContent')
# application.register_blueprint(avatar, url_prefix='/avatar')
# application.register_blueprint(avatar_polls, url_prefix='/voteforavatar')
# application.register_blueprint(grammar_content_details, url_prefix='/grammarcontentdetails')
# application.register_blueprint(comm_admin_portal, url_prefix='/CAP')
# application.register_blueprint(speech_to_text, url_prefix='/speech_to_text')
# application.register_blueprint(mock_test, url_prefix='/student_marks')
# application.register_blueprint(mock_ques, url_prefix='/mock_test')
# application.register_blueprint(coupon_validation, url_prefix='/coupon_validation')
# application.register_blueprint(insert_coins, url_prefix='/insert_coins')
# application.register_blueprint(contentwise_progress, url_prefix='/usercontentprogress')
# application.register_blueprint(product_rating, url_prefix='/product_rating')
# application.register_blueprint(string_to_audio, url_prefix='/string_to_audio')
# application.register_blueprint(cur_pre_portal, url_prefix='/cur_preview_portal')
# application.register_blueprint(parents_service, url_prefix='/parents_section')
# application.register_blueprint(report_analysis, url_prefix='/report_analysis')
# application.register_blueprint(admin_section, url_prefix='/admin_section')
# application.register_blueprint(job_portal, url_prefix='/job_portal')
# application.register_blueprint(spellbee, url_prefix='/spellbee')
# application.register_blueprint(otp_jobportal, url_prefix='/generate_otp')
# application.register_blueprint(myelsa_sms_mail, url_prefix='/myelsa_communication')
# application.register_blueprint(yrb_admin_portal, url_prefix='/yrb_admin_portal')
# application.register_blueprint(myelsa_registration, url_prefix='/myelsa_registration')
# application.register_blueprint(teacher_portal, url_prefix='/teacher_portal')
# application.register_blueprint(marks_n_remarks, url_prefix='/mock_feedback')
# application.register_blueprint(sales_app_subcription, url_prefix='/register_from_sales_app')
# application.register_blueprint(chatbot, url_prefix='/chatbot')
# application.register_blueprint(fee_management, url_prefix='/fee_management')
# application.register_blueprint(logindb_controller, url_prefix='/logindb_section')
# application.register_blueprint(games_section, url_prefix='/games_section')
# application.register_blueprint(mycomm_controller, url_prefix='/mycommunication')
# application.register_blueprint(student_subscription, url_prefix='/student_subscription')
# application.register_blueprint(cash_transaction, url_prefix='/cash_transaction')
# application.register_blueprint(user_library, url_prefix='/user_library')
# application.register_blueprint(live_classes, url_prefix='/live_classes')
# application.register_blueprint(user_library_assessments, url_prefix='/user_library_assessments')
# application.register_blueprint(teacher_to_institution, url_prefix='/register_teacher')
# application.register_blueprint(engagement_portal, url_prefix='/engagement_portal')

@application.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
	# application.register_blueprint(youngRB_blueprint)
	# application.register_blueprint(coupon)
	application.run()