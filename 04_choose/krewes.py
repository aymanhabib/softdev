"""
TNPG: VAT, Vivian Graeber, Ayman Habib, Talia Hsia

DISCO:

QCC:

OPS SUMMARY:

"""
import random
krewes = {2: ['agershkovich', 'ahabib', 'apiatetsky', 'atalukder', 'awong', 'bchen', 'cchen', 'dliu', 'dyentin', 'epaperno', 'fchen', 'fhuda', 'hwang', 'iyeung', 'jlee', 'jsong', 'jyuen', 'kxiao', 'mnelson', 'ntarsis', 'qsun', 'rtang', 'slubelsky', 'thsia', 'vgraeber', 'vsaboo', 'wliu', 'wvongphanith', 'yaziz', 'ylau', 'zjian'], 7:['afang30', 'egelobter30', 'jguo30', 'kliu31', 'myee30', 'scowan30', '
agarbutt268   eortiz30     jkwok30  kshekyan30  nhameed30     shua30
akatari30     gpark30      jwang31  llee30      nzhou30       snirloy30
btieu30       gthompson30  jwu31    mjiang30    pdey30        tzhang30
dakhmedova30  ijiang30     jyu30    mqiu30      rgoychayev30  vteo30
dchen30       jfeng31      kli30    mriki30     rmangar30     wguo30
], 8:[aalnasser30  byang30   frafee30  jli31       mmori30    sho30        wli30
ali34        dbi30     gmo30     jliu31      nabedin30  skusakabe30  wmach30
amehta30     dhe30     hbach30   jmohabir30  rlee30     sroy30       ychan30
ashifrina30  eli30     hzhu30    jtang30     sching30   swu30        yfeng30
bwang30      esohel30  jjeon30   kwang30     shaque30   vli30
]}
pd_list = [2, 7, 8]
pd = random.choice(pd_list)

name = random.choice(krewes[pd])

print(str(pd) + ' ' + name)

