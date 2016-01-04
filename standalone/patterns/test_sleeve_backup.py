        #elbow dart
        #SD1 = C.addPoint('SD1',  left(SEB, 0.3 * distance(SEB, SEM))) #elbow dart point
        #pnt = intersectLineRay(SUB, SEB, SD1, angleOfLine(SUB, SEB) - ANGLE90)
        #SD1.i = C.addPoint('SD1.i', intersectLineRay(SUB, SEB, SD1, angleOfLine(SD1, pnt) - angleOfDegree(8))) #elbow dart inside leg
        #SD1.o = C.addPoint('SD1.o', intersectLineRay(SUB, SEB, SD1, angleOfLine(SD1, pnt) + angleOfDegree(8))) #elbow dart outside leg 
        #foldDart(SD1, SEB) #creates SD1.m, SD1.oc, SD1.ic; dart folds up towards elbow                   

        #Sleeve C control points
        SCM.addInpoint(right(SCM, 0.33 * distance(SUM, s1)))
        s1.addOutpoint(polar(s1, 0.33 * distance(s1, SCM.inpoint), angleOfLine(s1, SCM.inpoint)))
        s1.addInpoint(polar(s1, 0.33 * distance(SUB, s1), angleOfLine(SCM.inpoint, s1)))
        SCM.addOutpoint(left(SCM, distance(SUM, s2) / 3.0))
        SUF.addInpoint(right(SUF, distance(SUF, s2) / 3.0))                                      
        #s2.addInpoint(polar(s2, 0.33 * distance(s2, SCM.outpoint), angleOfLine(s2, SCM.outpoint)))
        #s2.addOutpoint(polar(s2, 0.33 * distance(s2, SUF), angleOfLine(SCM.outpoint, s2)))                        
        s2.addInpoint(polar(s2, distance(s2, SCM.outpoint) / 3.0, angleOfLine(SUF.inpoint, SCM.outpoint)))
        s2.addOutpoint(polar(s2, distance(s2, SUF) / 3.0, angleOfLine(SCM.outpoint, SUF.inpoint)))                
                 
        #adjust back lower sleeve cap
        SUB.addOutpoint(left(SUB, distance(SUB, s1) / 3.0))                                   
        bl_sleevecap_length = curveLength(points2List(SUB, SUB.outpoint, s1.inpoint, s1))
        bl_diff = bl_armscye_length - bl_sleevecap_length
        while (abs(bl_diff) > 1.0):
            print("bl_diff=", bl_diff)                
            updatePoint(SUB, right(SUB, bl_diff)) #will move left if bl_diff < 0
            updatePoint(SUB.outpoint, left(SUB, distance(SUB, s1) / 3.0))
            updatePoint(s1.inpoint, polar(s1, distance(s1, SUB) / 3.0, angleOfLine(SCM.inpoint, s1)))
            bl_sleevecap_length = curveLength(points2List(SUB, SUB.outpoint, s1.inpoint, s1))        
            bl_diff = bl_armscye_length - bl_sleevecap_length        
        print("bl_diff final=", bl_diff)                                
                 
        #adjust front lower sleeve cap       
        fl_sleevecap_length = curveLength(points2List(s2, s2.outpoint, SUF.inpoint, SUF))
        fl_diff = fl_armscye_length - fl_sleevecap_length                        
        while (abs(fl_diff) > 1.0):
            print("fl_diff=", fl_diff)        
            updatePoint(SUF, left(SUF, fl_diff))
            updatePoint(SUF.inpoint, right(SUF, distance(SUF, s2) / 3.0))
            updatePoint(s2.inpoint, polar(s2, distance(SCM.outpoint, s2) / 3.0, angleOfLine(SUF.inpoint, SCM.outpoint)))            
            #updatePoint(s2.outpoint, polar(s2, distance(SUF, s2) / 3.0, angleOfLine(SCM.outpoint, s2)))
            updatePoint(s2.outpoint, polar(s2, distance(SUF.inpoint, s2) / 3.0, angleOfLine(SCM.outpoint, SUF.inpoint)))
            fl_sleevecap_length = curveLength(points2List(s2, s2.outpoint, SUF.inpoint, SUF))            
            fl_diff = fl_armscye_length - fl_sleevecap_length                 
        print("fl_diff final=", fl_diff)                     
 
        #front & back wrist
        SWB = C.addPoint('SWB', intersectLineRay(SD1.o, s3, s4, angleOfLine(SD1.o, s3) - ANGLE90)) #sleeve wrist back        
        SWF = C.addPoint('SWF', onLineAtLength(SUF, s5, distance(SUB, SD1.i) + distance(SD1.o, SWB))) #sleeve wrist front 
        #front elbow
        SEF = C.addPoint('SEF', onLineAtY(SUF, s5, SEM.y)) #sleeve elbow front                  

        #control points b/w SWF front wrist & SWB back wrist
        SWF.addOutpoint(polar(SWF, distance(SWF, SWB)/3.0, angleOfLine(SEF, SWF) - ANGLE90)) #handle is perpendicular to sleeve seam
        SWB.addInpoint(s4) #handle is perpendicular to sleeve seam  
        
        #wrist points
        s3 = C.addPoint('s3', right(SWM, CD.wrist / 2.0)) #back wrist reference point        
        s4 = C.addPoint('s4', right(SWM, distance(SWM, s3) / 3.0)) #back wrist middle reference point
        s5 = C.addPoint('s5', left(s3, 1.3 * CD.wrist)) #front wrist reference point plus 30% ease
        s6 = C.addPoint('s6', right(s5, distance(s5, SWM) / 3.0)) #front wrist middle reference point   
