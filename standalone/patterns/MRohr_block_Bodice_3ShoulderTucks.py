ó
©
·Tc           @   s\   d  d l  Td  d l Td  d l Td  d l m Z d  d l j Z d  d l j	 j
 Z d   Z d S(   iÿÿÿÿ(   t   *(   t   ClientNc         C   s#  t  j |  | | |  \ } } t   j |  t   j |  t t j t j  } t t j t j  d } t	 t
 t j t t j   d } | d }	 t d d  t d d  }
 } t | d t t d t   }
 t | d t |
 d t   } t | d t t t   |
 _ t | d |
 j  |
 _ t |
 j t d t  } t t j |  t t j |  t | d	 t |
 j t d t   | _ t | d
 | j  | _ t   } t t | t j |
 j |
 j | j | j t t j t j t t j t j t  t t | t j t j t t t | |
 	 t |
 | |
 j | j | j t t j t j t t j t j t t j t j t t t | |
  t | | | j t t j t j t t j t j t t j t j t t t |  t | t t  t | |
 t j  t | | |
 j  t | d t t j t t t   t _ t | d t t j t t t j t j    t _ t | d t |
 j |
 t t   |
 _ t | d t |
 j |
 t |
 j |
 j    |
 _ t | d t | j | t t   | _ t | d t | j | t | j | j    | _ t  t t t t!  d t" t t  t#  } t t! j |  t t! t t t!  d  } t t! j |  t  t$ t t$ t% j  d t" t& t$  t#  } t t% j j |  xZ t j j t j j t j' j t j' j t j j t j j f D] } t | t(  d | _) qóWt*   t   f S(   s   
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        g      @g       @t   namet   aD2t   aD3i   s   aD2.os   aD2.is   aD3.os   aD3.is   aD1.h1s   aD1.h2s   aD2.h1s   aD2.h2s   aD3.h1s   aD3.h2t    (+   t   BBt   patternt   globalst   updatet   pntMidPointPt   aD1t   it   ot	   distancePt   abst   angleOfVectorPt   Pntt   rPointPt   rightPointPt   INt   aht   agt
   pntOnLinePt   updatePointt   slashAndSpreadt   adt   c1t   c2t   amt   ajt   aot   akt   addDartFoldt   pntIntersectLinesPt   act   h1t   h2t   polarPointPt   abt   angleOfLinePt   ANGLE90t   bkt   bD1t   bjt   mt   apR   t   locals(   t   doct   At   Bt   CDt	   BB_localst
   BB_globalst   midpointt	   dartwidtht   rotate_anglet   dartwidth_halfR   R   t   pntt
   rotate_pnt(    (    sU   /home/susan/src/tmtp-private/standalone/patterns/MRohr_block_Bodice_3ShoulderTucks.pyR      sR    M"
(	L([L'3'3'3,/C(   t   tmtpl.constantst   tmtpl.patternt   tmtpl.documentt   tmtpl.clientR   t   pysvg.builderst   builderst   PYBt&   MRohr.blocks.MRohr_block_Bodice_Fittedt   blockst   MRohr_block_Bodice_FittedR   R   (    (    (    sU   /home/susan/src/tmtp-private/standalone/patterns/MRohr_block_Bodice_3ShoulderTucks.pyt   <module>   s   


