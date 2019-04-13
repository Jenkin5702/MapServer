from django.conf.urls import url
from . import view,testdb,search,search2
 
urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
    url(r'^login$', testdb.check_login),
    url(r'^register$', testdb.register),
    url(r'^pub_commu$', testdb.pub_communicate),
    url(r'^load_commu$', testdb.load_communicate),
    url(r'^new_delegate$', testdb.new_delegate),
    url(r'^load_delegate$', testdb.load_delegate),
    url(r'^load_notif$', testdb.load_notif),
    url(r'^zan_plus$', testdb.zanPlus),
    url(r'^zan_minus$', testdb.zanMinus),
    url(r'^join$', testdb.join),
    url(r'^leave$', testdb.leave),
    url(r'^peoplenum$', testdb.peoplenum),
    url(r'^del_delegate$', testdb.del_delegate),
    url(r'^msg_after$', testdb.msg_after),
]