#!/usr/bin/env python
# library_Mens_Classic_Shirt_Aldrich.py
# library pattern no. ML1
# This is a library pattern to be used to make other patterns

from pysvg.builders import path
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.constants import *
from tmtpl.utils import *

class PatternDesign():

    def __init__(self):
        self.styledefs = {}
        self.markerdefs = {}
        return

    def pattern(self):
        """
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        """
        # All measurements are converted to pixels
        # x increases towards right, y increases towards bottom of drawing - Quadrant is 'upside down'
        # All angles are in radians
        # angles start with 0 at '3:00', & move clockwise b/c quadrant is 'upside down'

        CD = self.CD #client data is prefaced with CD
        printer = '36" wide carriage plotter'
        patternData = { 'companyName' : 'Seamly Patterns', # mandatory
            'designerName' : 'Winifred Aldrich',  # mandatory
            'patternTitle'  :'Mens Classic Shirt', # mandatory
            'patternNumber' : 'Ald-MS-1' # mandatory
        }
        #create document
        doc = setupPattern(self,  CD,  printer,  patternData)

        # create pattern object, add to document
        shirt = Pattern('shirt')
        shirt.styledefs.update(self.styledefs)
        shirt.markerdefs.update(self.markerdefs)
        doc.add(shirt)

        # create pattern pieces, add to pattern object
        shirt.add(PatternPiece('pattern', 'yoke', 'A', fabric=2, interfacing=0, lining=0))
        shirt.add(PatternPiece('pattern', 'back', 'B', fabric=2, interfacing=0, lining=0))
        shirt.add(PatternPiece('pattern', 'front', 'C', fabric=2, interfacing=0, lining=0))
        shirt.add(PatternPiece('pattern', 'sleeve', 'D', fabric=2, interfacing=0, lining=0))
        shirt.add(PatternPiece('pattern', 'cuff', 'E', fabric=2, interfacing=0, lining=0))
        shirt.add(PatternPiece('pattern', 'collarstand', 'F', fabric=2, interfacing=0, lining=0))
        shirt.add(PatternPiece('pattern', 'collar', 'G', fabric=2, interfacing=0, lining=0))
        A = shirt.yoke
        B = shirt.back
        C = shirt.front
        D = shirt.sleeve
        E = shirt.cuff
        F = shirt.collarstand
        G = shirt.collar

        SHIRT_LENGTH = 80*CM

        a = Pnt(0.0, 0.0) # nape
        b = Pnt(a.x, a.y + CD.back_armfold_balance) # lowers sleeve's underarm point
        print(b.x,  b.y)
        c = Pnt(a.x, a.y + CD.back_waist_length + 2.5*CM + 3*CM) #natural waist = 1" below waistline
        d = Pnt(a.x, a.y + SHIRT_LENGTH + 8*CM)
        e = Pnt(a.x + CD.bust/2.0 + 12*CM, b.y)
        print(e.x, e.y)
        f = Pnt(e.x, a.y)
        g = Pnt(e.x, d.y)
        h = Pnt(a.x + (CD.neck/5.0 - 0.5*CM), a.y)
        i = Pnt(h.x, h.y - 4.5*CM)
        j = Pnt(a.x, a.y + distance(a,b)/5.0 + 2*CM)
        k = Pnt(a.x + CD.back_armfold_distance/2.0 + 4*CM, j.y)
        l = Pnt(k.x, b.y)
        m = Pnt(k.x, a.y)
        n = Pnt(m.x + 0.75*CM, m.y - 2*CM)
        #o = Pnt(k.x - (10*CM), k.y)
        temp_ll = Pnt(j.x - 2*CM, j.y)
        o = midPoint(temp_ll, k) # midpoint b/w ll (defined below) & k
        p = Pnt(k.x, k.y + 0.75*CM)
        temp1 = b.x
        temp2 = distance(b, e)/2.0
        temp3 = 0.5*CM
        q = Pnt(temp1 + temp2 + temp3, b.y)
        r = Pnt(q.x, c.y)
        s = Pnt(q.x, d.y)
        t = Pnt(f.x, f.y + 4.5*CM)
        u = Pnt(t.x - (CD.neck/5.0 - 1*CM), t.y)
        v = Pnt(t.x, t.y + (CD.neck/5.0 - 2.5*CM))
        w = Pnt(k.x, k.y + 1.5*CM)
        pnts = onCircleAtY(u, distance(i,n) + 0.5*CM, w.y)
        if (pnts[0].x < u.x): # if 1st intersection is to the left of u
            x = PntP(pnts[0])
        else:
            x = PntP(pnts[1])
        y = Pnt(b.x + (CD.bust/3.0 + 4.5*CM), e.y)
        z = Pnt(y.x, y.y - (3*CM))
        pnt = midPoint(z, x)
        aa = Pnt(pnt.x + (1*CM), pnt.y)
        bb = Pnt(v.x + (1.5*CM), v.y)
        cc = Pnt(bb.x + (3.5*CM), v.y)
        dd = Pnt(r.x + (2*CM), r.y)
        ee = Pnt(r.x - (2*CM), r.y)
        ff = Pnt(s.x, s.y - (20*CM))
        gg = Pnt(ff.x + (1*CM), ff.y)
        hh = Pnt(ff.x - (1*CM), ff.y)
        ii = onLineAtLength(g, s, distance(g,s)/2.0)
        jj = onLineAtLength(d,s,distance(d,s)/2.0)
        kk = Pnt(ii.x, ii.y - (4*CM))
        ll = PntP(temp_ll)
        mm = polar(l, 3*CM, angleOfDegree(315))
        nn = polar(y, 1.75*CM, angleOfDegree(225))
        oo = Pnt(ll.x, d.y)
        pp = Pnt(cc.x, kk.y)
        qq = Pnt(bb.x, kk.y)
        rr = Pnt(v.x, kk.y)
        ss = PntP(q)
        tt = onLineAtLength(w, l, distance(w, l)*0.5)
        uu = Pnt(i.x, a.y)
        vv = polar(uu, 2*CM, angleOfDegree(225))

        # control points for A yoke
        vv_c1 = Pnt(a.x + distance(a, vv)/3.0, a.y)
        vv_c2 = polar(vv, distance(a, vv)/3.0, angleOfDegree(135))
        i_c1 = polar(vv, distance(vv, i)/3.0, angleOfDegree(315))
        i_c2 = polar(i, distance(vv, i)/3.0, angleOfLine(i, n) + ANGLE90) #c2 is perpendicular to shoulder seam
        length1 = distance(k, n)/3.0
        k_c2 = onLineAtLength(k, m, length1)
        k_c1 = onLineAtLength(n, k_c2, length1)
        #control points for B back
        mm_c1 = onLineAtLength(tt, l, distance(tt, mm)/3.0)
        #mm_c2 = cPoint(B, 'mm_c2', onLineAtLength(mm, mm_c1, distance(tt, mm)/3.0))
        mm_c2 = polar(mm, distance(tt, mm)/3.0, angleOfDegree(225))
        ss_c2 = onLineAtLength(ss, l, distance(ss, mm)/3.0)
        ss_c1 = polar(mm, distance(ss, mm)/3.0, angleOfDegree(45))
        #ss_c1 = cPoint(B, 'ss_c1', onLineAtLength(mm, ss_c2, distance(ss, mm)/3.0))
        knots = pointList(ss, ee, hh)
        c1, c2 = controlPoints('back_side_seam_control_points', knots )
        ee_c1 = PntP(c1[0])
        ee_c2 = PntP(c2[0])
        hh_c1 = PntP(c1[1])
        hh_c2 = PntP(c2[1])
        jj_c1 = Pnt(hh.x - distance(hh, jj)/3.0, hh.y)
        jj_c2 = Pnt(jj.x + distance(hh, jj)/3.0, jj.y)
        p_c1 = Pnt(o.x + distance(o, p)/3.0, o.y)
        p_c2 = polar(p, distance(o, p)/3.0, angleOfLine(p, p_c1))
        #control points for C front
        x_c1 = polar(nn, distance(nn, x)/3.0, angleOfDegree(325))
        x_c2 = polar(x, distance(nn, x)/3.0, angleOfLine(x, x_c1))
        v_c1 = polar(u, distance(u, v)/3.0, angleOfLine(x, u) + ANGLE90)
        v_c2 = Pnt(v.x - distance(u, v)/3.0 + 1*CM,  v.y)
        q_c1 = polar(dd, distance(dd, q)/3.0, angleOfLine(gg, q))
        q_c2 = polar(q, distance(dd, q)/3.0, angleOfLine(q, q_c1))
        dd_c2 = polar(dd, distance(gg, dd)/3.0, angleOfLine(q, gg))
        dd_c1 = polar(gg, distance(gg, dd)/3.0, angleOfLine(gg, dd_c2))
        gg_c1 = polar(kk, distance(kk, gg)/3.0, ANGLE180)
        gg_c2 = polar(gg, distance(kk, gg)/3.0, angleOfDegree(0))
        nn_c1 = Pnt(q.x + distance(q, nn)/3.0, q.y)
        nn_c2 = polar(nn, distance(q, nn)/3.0, angleOfDegree(135))

        # E - cuff
        ca = Pnt(0.0, 0.0)
        cb = Pnt(ca.x + 25.5*CM, ca.y)
        cd1 = Pnt(ca.x - 3*CM, ca.y)
        ce = Pnt(cb.x + 3*CM, ca.y)
        cf = Pnt(ca.x, ca.y + 7.5*CM)
        cg = Pnt(cb.x, cf.y)
        ch = Pnt(cd1.x, cf.y - 3*CM)
        ci = Pnt(ce.x, cg.y - 3*CM)
        # control points for cuff
        cg_c1 = Pnt(ci.x, ci.y + distance(ci, cg)/3.0)
        cg_c2 = Pnt(cg.x + distance(ci, cg)/3.0, cg.y)
        ch_c1 = Pnt(cf.x - distance(cf, ch)/3.0, cf.y)
        ch_c2 = Pnt(ch.x, ch.y + distance(cf, ch)/3.0)

        # D - sleeve, based on A,B,C points
        cArray1 = pointList(tt, mm_c1, mm_c2, mm,  ss_c1, ss_c2, ss, nn_c1, nn_c2, x)
        cArray2 = pointList(n, k_c1, k_c2, k)
        armscyeLength = curveLength(cArray1) + curveLength(cArray2)
        cuffDepth = (cf.y - ca.y)

        sa = Pnt(0.0, 0.0)
        sb = Pnt(sa.x, sa.y + armscyeLength/4.0 + 1.5*CM)
        sc = Pnt(sa.x, sa.y + CD.oversleeve_length + 6*CM - cuffDepth )
        sd = midPoint(sb, sc)
        se = Pnt(sb.x - (armscyeLength/2.0 - 0.5*CM), sb.y)
        sf = Pnt(se.x, sc.y)
        sg = Pnt(sb.x + (armscyeLength/2.0 - 0.5*CM), sb.y)
        sh = Pnt(sg.x, sc.y)

        angle = angleOfLine(se, sa)
        pnt = onLineAtLength(se, sa, distance(se, sa)/4.0)
        si = onLineAtLength(se, sa, distance(se, sa)/4.0)
        pnt = onLineAtLength(se, sa, distance(se, sa)/2.0)
        sj = polar(pnt, 1*CM, angle + angleOfDegree(-90))
        pnt = onLineAtLength(se, sa, 0.75*distance(se, sa))
        sk = polar(pnt, 2*CM, angle + angleOfDegree(-90))

        angle = angleOfLine(sg, sa)
        pnt = onLineAtLength(sg, sa, distance(sg, sa)/4.0)
        sl = polar(pnt, 1*CM, angle + angleOfDegree(-90))
        sm = onLineAtLength(sg, sa, distance(sg, sa)/2.0)
        pnt = onLineAtLength(sg, sa, 0.75*distance(sg, sa))
        sn = polar(pnt, 1*CM, angle + ANGLE90)

        so = onLineAtLength(sf, sc, distance(sf, sc)/3.0)
        sp = onLineAtLength(sh, sc, distance(sh, sc)/3.0)
        sq = midPoint(sf,so)
        sr = midPoint(sh,sp)
        st = midPoint(sc,so)
        su = Pnt(st.x, st.y - 15*CM)
        sv = Pnt(st.x, st.y + 1*CM)
        sw = onLineAtY(se, sq, sd.y)
        sx = onLineAtY(sg, sr, sd.y)
        sy = midPoint(sb, sd)
        sz = onLineAtY(se, sq, sd.y)
        # control points for sleeve
        cArray = pointList(se, si, sj, sk, sa, sn, sm, sl, sg)
        c1, c2 = controlPoints('sleeve_cap', cArray)
        si_c1, si_c2 = PntP(c1[0]), PntP(c2[0])
        sj_c1, sj_c2 = PntP(c1[1]), PntP(c2[1])
        sk_c1,  sk_c2 = PntP(c1[2]), PntP(c2[2])
        sa_c1, sa_c2 = c1[3], c2[3]
        sn_c1,  sn_c2 = c1[4], c2[4]
        sm_c1, sm_c2 = c1[5], c2[5]
        sl_c1,  sl_c2 = c1[6], c2[6]
        sg_c1, sg_c2 = c1[7], c2[7]
        cArray = pointList(so, sw, se)
        c1, c2 = controlPoints('sleeve_seam1', cArray)
        sw_c1, sw_c2 = c1[0], c2[0]
        se_c1, se_c2 = c1[1], c2[1]
        cArray = pointList(sg, sx, sp)
        c1, c2 = controlPoints('sleeve_seam2', cArray)
        sx_c1, sx_c2 = c1[0], c2[0]
        sp_c1, sp_c2 = c1[1], c2[1]
        cArray = pointList(sc, sv, so)
        c1, c2 = controlPoints('sleeve_placket', cArray)
        sv_c1, sv_c2 = c1[0], c2[0]
        so_c1, so_c2 = c1[1], c2[1]


        # F & G --> collar stand & collar -  G is drawn from points on F
        ka = Pnt(0.0, 0.0)
        curve1 = pointList(a, i_c1, i_c2,  i)
        curve2 = pointList(u, v_c1, v_c2, v)
        kb = Pnt(ka.x + (curveLength(curve1) + curveLength(curve2)), ka.y)
        kc = Pnt(kb.x + (1.5*CM + 1.25*CM), ka.y)
        kd = Pnt(ka.x + (distance(ka,kb)*3/4.0), ka.y)
        ke = Pnt(ka.x, ka.y - (8*CM + 2*CM))
        kf = midPoint(ka, ke)
        kg = Pnt(kb.x, kf.y)
        kh = Pnt(kc.x, kf.y)
        ki = Pnt(kh.x - (1*CM), kf.y)
        kj = onLineAtLength(kc, ki, 0.75*CM)
        kl = onLineAtLength(ki, kc, 0.75*CM)
        km = Pnt(ka.x, ka.y - 0.5*CM)
        kn = midPoint(kf, kg)
        ko = Pnt(kg.x, kg.y + 1*CM)
        kp = onLineAtLength(kl, kc, 1*CM)
        kq = Pnt(kg.x + 1*CM, ke.y - 1*CM)
        kr = Pnt(kn.x, ke.y)
        #ks = pntOnCurveX(d,j,b.x)
        ks = Pnt(kb.x, kj.y + 0.4*CM)
        # control points for collar
        cArray = pointList(km, kd, ks, kj)
        c1, c2 = controlPoints('collar_stand_bottom', cArray)
        kd_c1, kd_c2 = c1[0], c2[0]
        ks_c1, ks_c2 = c1[1],  c2[1]
        kj_c1, kj_c2 = c1[2],  c2[2]

        cArray = pointList(kp, ko, kn)
        c1, c2 = controlPoints('collar_stand_top', cArray)
        kn_c2 = Pnt(kn.x + distance(ko, kn)/2.0, kn.y)
        kn_c1 = onLineAtLength(ko, kn_c2, distance(ko, kn_c2)/2.0)
        ko_c2 = onLineAtLength(ko, kn_c2, -distance(kp, ko)/3.0)
        ko_c1 = onLineAtLength(kp, ko_c2, distance(kp, ko)/3.0)
        kq_c1 = Pnt(kr.x + distance(kr, kq)/3.0, kr.y)
        kq_c2 = polar(kq, distance(kr, kq)/3.0, angleOfLine(kq, kq_c1))

        # ------------------------------------------------ #
        # ----- all points defined, now define paths ----- #
        # ------------------------------------------------ #

        # shirt Yoke A
        #grainline coords
        Ag1 = Pnt(h.x + 1*CM, h.y - 2*CM)
        Ag2 = Pnt(Ag1.x, j.y - 1*CM)
        (A.label_x, A.label_y) = (Ag1.x + 1*CM, Ag1.y + 1*CM)

        # Set letter location and size
        # optional arguments to setLetter:
        # style = 'letter_text_style' (defaults to default_letter_text_style)
        # text = 'D' (or whetever you want. Defaults to the letter set when creating the pattern piece)
        # scaleby = a factor to scale the letter by
        A.setLetter(x = Ag1.x + 7*CM, y = Ag2.y, scaleby=10.0)

        # gridline
        grid = path()
        addToPath(grid, 'M', a, 'L', j, 'L', k, 'L', m, 'L', a, 'M', i, 'L', h, 'M', uu, 'L', vv)
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', a, 'C', vv_c1, vv_c2, vv,'C', i_c1, i_c2,  i, 'L',  n, 'C', k_c1, k_c2, k, 'L', j, 'L', a)
        # add grid, grainline, seamline & cuttingline paths to pattern
        addGrainLine(A, Ag1, Ag2)
        addGridLine(A, grid)
        addSeamLine(A, seamLine)
        addCuttingLine(A, cuttingLine)

        # shirt Back B
        #grainline points
        Bg1 = Pnt(i.x,  j.y + 8*CM)
        Bg2 = Pnt(Bg1.x, d.y - 8*CM)
        # label points
        B.label_x,  B.label_y = Bg1.x + 3*CM, Bg1.y  + 3*CM
        # Set letter location and size
        B.setLetter(x = o.x, y = ee_c2.y, scaleby=15.0)
        # gridline
        grid = path()
        addToPath(grid, 'M', j, 'L', d, 'M', ll, 'L', oo, 'M', p, 'L', l, 'L', mm, 'M', ss, 'L', s) #vertical
        addToPath(grid, 'M', ll, 'L', k, 'M', b, 'L', ss, 'M', c, 'L', r, 'M', oo, 'L', s) #horizontal
        # foldLine
        foldLine = path()
        addToPath(foldLine, 'M', ll, 'L', oo)
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', ll, 'L', o, 'C', p_c1, p_c2, p, 'L', tt, 'C', mm_c1, mm_c2, mm, 'C', ss_c1, ss_c2, ss)
            addToPath(P, 'C', ee_c1, ee_c2, ee, 'C', hh_c1, hh_c2, hh, 'C', jj_c1, jj_c2, jj, 'L',  oo, 'L', ll)
        # add grid, grainline, seamline & cuttingline paths to pattern
        addGrainLine(B, Bg1, Bg2)
        addGridLine(B, grid)
        addFoldLine(B, foldLine)
        addSeamLine(B, seamLine)
        addCuttingLine(B, cuttingLine)

        # shirt Front C
        #grainline points
        Cg1 = Pnt(u.x - 1*CM, u.y + 8*CM)
        Cg2 = Pnt(Cg1.x, g.y - 8*CM)
        # label points
        C.label_x,  C.label_y = Cg1.x - 8*CM, Cg1.y + 3*CM
        # Set letter location and size
        C.setLetter(x = x_c1.x, y = dd.y, scaleby=15.0)
        # grid
        grid = path()
        addToPath(grid, 'M', ss, 'L', s, 'M', x, 'L', z, 'L', y, 'L', nn,'M', kk, 'L', ii, 'M', f, 'L', g, 'M', bb, 'L', qq, 'M', cc, 'L', pp) #vertical
        addToPath(grid, 'M', f, 'M', u, 'L', t, 'M', v, 'L', cc, 'M', ss, 'L', e, 'M', r, 'L', dd, 'M', ff, 'L', gg, 'M', s, 'L', g) #horizontal
        # fold line
        foldLine = path()
        addToPath(foldLine, 'M', bb, 'L', qq)
        # marking line
        markingLine = path()
        addToPath(markingLine, 'M', v, 'L', rr)
        #seam line & cutting line
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', u, 'C', v_c1, v_c2, v, 'L', bb, 'L', cc, 'L', pp, 'L', kk, 'C', gg_c1, gg_c2, gg, 'C', dd_c1, dd_c2, dd, 'C', q_c1, q_c2, q, 'C', nn_c1, nn_c2, nn, 'C', x_c1, x_c2, x, 'L', u)
        # add grid, grainLine, seamLine & cuttingLine paths to pattern
        addGrainLine(C, Cg1, Cg2)
        addGridLine(C, grid)
        addFoldLine(C, foldLine)
        addMarkingLine(C, markingLine)
        addSeamLine(C, seamLine)
        addCuttingLine(C, cuttingLine)

        # shirt Sleeve D
        #grainline points
        Dg1 = Pnt(sb.x, sb.y)
        Dg2 = Pnt(Dg1.x, sc.y - 8*CM)
        # label points
        D.label_x,  D.label_y = Dg1.x + 3*CM, Dg1.y + 8*CM
        # Set letter location and size
        D.setLetter(x = sj_c1.x, y = sy.y, scaleby=15.0)
        # gridline
        grid = path()
        addToPath(grid, 'M',sa,'L', sc, 'M', sg, 'L', sh, 'M', se, 'L', sf, 'M', su,  'L', sv) # vertical
        addToPath(grid, 'M', se, 'L', sa, 'L',  sg, 'M', se, 'L', sq, 'M', sw, 'L', so, 'M', sg, 'L', sr, 'M', sx, 'L', sp) #diagonal
        addToPath(grid, 'M', se, 'L', sg,  'M', sw, 'L', sx, 'M', sf, 'L', sh) #horizontal
        # marking line
        markingLine = path()
        addToPath(markingLine, 'M', su, 'L', sv)
        # seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', se, 'C', si_c1, si_c2, si, 'C', sj_c1, sj_c2, sj, 'C', sk_c1, sk_c2, sk, 'C', sa_c1, sa_c2, sa)
            addToPath(P, 'C', sn_c1, sn_c2, sn, 'C', sm_c1, sm_c2, sm, 'C', sl_c1, sl_c2, sl, 'C', sg_c1, sg_c2, sg)
            addToPath(P,  'C', sx_c1, sx_c2, sx, 'C', sp_c1, sp_c2, sp, 'L', sc, 'C', sv_c1, sv_c2, sv, 'C', so_c1, so_c2, so)
            addToPath(P, 'C', sw_c1, sw_c2, sw, 'C', se_c1, se_c2, se)
        # add grid, grainline, seamline & cuttingline paths to pattern
        addGridLine(D, grid)
        addGrainLine(D, Dg1, Dg2)
        addMarkingLine(D, markingLine)
        addSeamLine(D, seamLine)
        addCuttingLine(D, cuttingLine)

        # shirt Cuff E
        #grainline points
        Eg1 = Pnt(ca.x + 2*CM,  ca.y + 2*CM)
        Eg2 = Pnt(cb.x - 2*CM, Eg1.y)
        # label points
        E.label_x,  E.label_y = Eg1.x + 3*CM, Eg1.y + 1*CM
        # Set letter location and size
        E.setLetter(x = (Eg1.x+Eg2.x)/2.0, y = (ch_c1.y+ch_c2.y)/2.0, scaleby=7.0)
        # gridline
        grid = path()
        addToPath(grid, 'M', cd1,'L', ch, 'M', ca, 'L', cf, 'M', cb, 'L', cg, 'M', ce,  'L', ci) # vertical
        addToPath(grid, 'M', cd1, 'L', ce,  'M', cf, 'L', cg) #horizontal
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', cd1, 'L', ce, 'L', ci, 'C', cg_c1, cg_c2, cg, 'L', cf, 'C', ch_c1, ch_c2, ch, 'L', cd1)
        # add grid, grainline, seamline & cuttingline paths to pattern
        addGrainLine(E, Eg1, Eg2)
        addGridLine(E, grid)
        addSeamLine(E, seamLine)
        addCuttingLine(E, cuttingLine)

        # shirt Collar Stand F
        #grainline points
        Fg1 = Pnt(ka.x + 2*CM, ka.y - 1*CM)
        Fg2 = Pnt(kb.x - 2*CM, Fg1.y)
        # label points
        F.label_x,  F.label_y = Fg1.x + 1*CM, kf.y + 1*CM
        # Set letter location and size
        F.setLetter(x = kn.x, y = Fg1.y - 1*CM, scaleby=5.0)
        # gridline
        grid = path()
        addToPath(grid, 'M', ke,'L', ka, 'M', kg, 'L', kb, 'M', kh, 'L', kc) # vertical
        addToPath(grid, 'M', km, 'L', kd, 'L', ks, 'L',kj,'M', kc, 'L', ki, 'M', kp, 'L', ko, 'L', kn, 'M', kr, 'L', kq, 'L', ko)
        addToPath(grid, 'M', ke, 'L', kr,  'M', kf, 'L', kh, 'M', ka, 'L', kc) #horizontal
        # fold line
        foldLine = path()
        addToPath(foldLine, 'M', kf, 'L', km)
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', kf, 'L', km, 'C', kd_c1, kd_c2, kd, 'C', ks_c1, ks_c2, ks, 'C', kj_c1, kj_c2, kj, 'L', kp, 'C', ko_c1, ko_c2, ko, 'C', kn_c1, kn_c2, kn, 'L', kf)
        # add grid, grainline, seamline & cuttingline paths to pattern
        addGrainLine(F, Fg1, Fg2)
        addGridLine(F, grid)
        addFoldLine(F, foldLine)
        addSeamLine(F, seamLine)
        addCuttingLine(F, cuttingLine)

        # shirt Collar G
        #grainline points
        Gg1 = Pnt(ke.x + 1*CM, ke.y + 1*CM)
        Gg2 = Pnt(kg.x - 1*CM, Gg1.y)
        # label points
        G.label_x,  G.label_y = Gg1.x + 1*CM, Gg1.y + 1*CM
        # Set letter location and size
        G.setLetter(x = (Gg1.x+Gg2.x)/2.0, y = Gg1.y + 3*CM, scaleby=5.0)
        # fold line
        foldLine = path()
        addToPath(foldLine, 'M', ke, 'L', kf)
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', kf, 'L', ke, 'L', kr, 'C', kq_c1, kq_c2, kq, 'L', ko, 'C', kn_c1, kn_c2, kn, 'L', kf)
        # add grid, grainline, seamline & cuttingline paths to pattern
        addGrainLine(G, Gg1, Gg2)
        # no grid for collar, included in collar stand pattern piece F
        addFoldLine(G, foldLine)
        addSeamLine(G, seamLine)
        addCuttingLine(G, cuttingLine)


        # call draw once for the entire pattern
        doc.draw()
        return
# vi:set ts=4 sw=4 expandtab:

