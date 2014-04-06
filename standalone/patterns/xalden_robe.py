{
  "pattern": {
    "pattern_number": "C_KH_Xalden",
    "title": "Xaldin Robe",
    "summary": {
        "category": "Cosplay",
        "anime": "Kingdom Hearts",
        "tags": [
            "Kingdom Hearts",
            "Xaldin",
            "Robe"
        ],
        "description": "Long-sleeved robe with front zipper closing, inset hip-level pockets, oversized hood, and sleeves widened towards wrists. Based on Xaldin character from Kingdom Hearts.",
        "recommended": {
            "fabric": "Leather, pleather, sweatshirt fabric, or any heavy-weight tightly woven fabric with good drape characteristics.",
            "notions": "Oversized #30 molded plastic zipper specially made by YKK for Nobody characters in Kingdom Hearts."
        }
    },
    "measurements": [
        "height",
        "head_and_neck_length",
        "neck",
        "neck_diameter",

        "shoulder_length",

        "across_chest",
        "across_back",

        "front_highbust_width",
        "front_highbust_height",
        "back_highbust_width",
        "back_highbust_height",

        "bust",
        "front_bust_width",
        "front_bust_height",
        "back_bust_width",
        "back_bust_height",

        "waist",
        "front_waist_width",
        "back_waist_width",
        "side_waist_length",
        "front_waist_length",
        "back_waist_length",

        "hip",
        "front_hip_width",
        "back_hip_width",
        "back_hip_height",
        "side_hip_height",
        "hip_to_floor",

        "front_neck_balance",
        "back_neck_balance",
        "front_shoulder_balance",
        "back_shoulder_balance",

        "overarm_length",
        "hand_length",
        "ankle_to_floor"
    ],

    "main" : [
        {
          "id" : "Coat Back A",
          "type" : "path",
          "d" : [
            ["M", "pt.backNeckCenter" ],
            ["L", "pt.backWaistCenter" ],
            ["C", "pt.bWC_out", "pt.bHipC_in", "pt.backHipCenter" ],
            ["L", "pt.backHemCenter" ],
            ["C", "pt.bHemC_out", "pt.bHemS_in", "pt.backHemSide" ],
            ["L", "pt.backHipSide" ],
            ["C", "pt.bHipS_out", "pt.bWS_in", "pt.backWaistSide" ],
            ["C", "pt.bWS_out", "pt.bBS_in", "pt.backBustSide" ],
            ["C", "pt.bBS_out", "pt.bArm_in", "pt.backArmscye" ],
            ["C", "pt.bArm_out", "pt.bSTin", "pt.backShoulderTip" ],
            ["L", "pt.backNeckSide" ],
            ["C", "pt.bNS_out", "pt.bNC_in", "pt.backNeckCenter" ],
            ["z"]
          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"3", "stroke":"#000000", "fill":"none" }
        },
        {
          "id" : "Coat Upper Front B",
          "type" : "path",
          "d" : [
            ["M", "pt.frontNeckCenter" ],
            ["L", "pt.b13" ],
            ["C", "pt.b13out", "pt.b19in", "pt.b19" ],
            ["C", "pt.b19out", "pt.b14in", "pt.b14" ],
            ["C", "pt.b14out", "pt.b15in", "pt.b15" ],
            ["L", "pt.b17" ],
            ["L", "pt.b18" ] ,
            ["L", "pt.b10" ] ,
            ["C", "pt.b10out", "pt.b12in", "pt.b12" ],
            ["C", "pt.b12out", "pt.fUnd_in", "pt.frontUnderarm" ],
            ["C", "pt.fUnd_out", "pt.fArm_in", "pt.frontArmscye" ],
            ["C", "pt.fArm_out", "pt.b20in", "pt.b20" ],
            ["L", "pt.frontNeckSide" ],
            ["C", "pt.fNS_out", "pt.fNC_in", "pt.frontNeckCenter" ],
            ["z"]
          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"3", "stroke":"#000000", "fill":"none" }
        },
        {
          "id" : "Coat Lower Front C",
          "type" : "path",
          "d" : [
            ["M", "pt.c1" ],
            ["L", "pt.c2" ],
            ["L", "pt.c3" ],
            ["C", "pt.c3out", "pt.c4in", "pt.c4" ],
            ["L", "pt.c5" ],
            ["L", "pt.c6" ],
            ["C", "pt.c6out", "pt.c7in", "pt.c7" ],
            ["C", "pt.c7out", "pt.c8in", "pt.c8" ],
            ["C", "pt.c8out", "pt.c1in", "pt.c1" ],
            ["z"]
          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"3", "stroke":"#000000", "fill":"none" }
        },
        {
          "id" : "Coat Pocket Lining G",
          "type" : "path",
          "d" : [
            ["M", "pt.g1" ],
            ["L", "pt.g2" ],
            ["L", "pt.g3" ],
            ["L", "pt.g4" ],
            ["L", "pt.g1" ],
            ["z"]
          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"3", "stroke":"#000000", "fill":"none" }
        },
        {
          "id" : "Coat Pocket Flap H",
          "type" : "path",
          "d" : [
            ["M", "pt.h1" ],
            ["L", "pt.h2" ],
            ["L", "pt.h3" ],
            ["L", "pt.h4" ],
            ["L", "pt.h1" ],
            ["z"]
          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"3", "stroke":"#000000", "fill":"none" }
        },
        {
          "id" : "Coat Hood Side D",
          "type" : "path",
          "d" : [
            ["M", "pt.d1" ],
            ["C", "pt.d1out", "pt.d6in", "pt.d6" ],
            ["C", "pt.d6out", "pt.d7in", "pt.d7" ],
            ["L", "pt.d4" ],
            ["L", "pt.d8" ],
            ["C", "pt.d8out", "pt.d9in", "pt.d9" ],
            ["L", "pt.d10" ],
            ["L", "pt.d1" ],
            ["z"]
          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"3", "stroke":"#000000", "fill":"none" }
        },
        {
          "id" : "Coat Hood Center E",
          "type" : "path",
          "d" : [
            ["M", "pt.e1" ],
            ["L", "pt.e2" ],
            ["L", "pt.e3" ],
            ["L", "pt.e4" ],
            ["L", "pt.e1" ],
            ["z"]
          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"3", "stroke":"#000000", "fill":"none" }
        },
        {
          "id" : "Sleeve F",
          "type" : "path",
          "d" : [
            ["M", "pt.f5" ],
            ["C", "pt.f5out", "pt.f1in", "pt.f1" ],
            ["C", "pt.f1out", "pt.f7in", "pt.f7" ],
            ["L", "pt.f12" ],
            ["C", "pt.f12out", "pt.f14in", "pt.f14" ],
            ["C", "pt.f14out", "pt.f3in", "pt.f3" ],
            ["C", "pt.f3out", "pt.f13in", "pt.f13" ],
            ["C", "pt.f13out", "pt.f11in", "pt.f11" ],
            ["L", "pt.f5" ],
            ["z"]
          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"3", "stroke":"#000000", "fill":"none" }
        }
    ],

    "construction": [
        { "id" : "Back Construction Lines",
          "type": "path",
          "d" : [
            ["M", "pt.backNeckCenter" ],
            ["L", "pt.backNeckSide" ],
            ["L", "pt.t1_bST" ],
            ["L", "pt.backAcrossSide" ],
            ["L", "pt.t1_bHS" ],
            ["L", "pt.t1_bBS" ],
            ["L", "pt.t1_bWS" ],
            ["L", "pt.t1_bHipS"],
            ["L", "pt.t1_bHipC"],
            ["L", "pt.backNeckCenter" ]

          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"2", "stroke":"#00FF00", "fill":"none" }
        },
        { "id" : "Back Measurement Lines",
          "type": "path",
          "d" : [
            ["M", "pt.backNeckCore" ],
            ["L", "pt.backNeckSide" ],
            ["M", "pt.backAcrossCenter" ],
            ["L", "pt.backAcrossSide" ],
            ["M", "pt.backHighbustCenter" ],
            ["L", "pt.backHighbustSide" ],
            ["M", "pt.backBustCenter" ],
            ["L", "pt.backBustSide" ],
            ["M", "pt.backWaistCenter" ],
            ["L", "pt.t1_bWS" ],
            ["M", "pt.backHipCenter" ],
            ["L", "pt.backHipSide" ]

          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"2", "stroke":"#FF0000", "fill":"none" }
        },
        { "id" : "Back Balance Lines",
          "type": "path",
          "d" : [
            ["M", "pt.backWaistCenter" ],
            ["L", "pt.backNeckSide" ],
            ["M", "pt.backWaistCenter" ],
            ["L", "pt.t1_bST" ]

          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"2", "stroke":"#0000FF", "fill":"none" }
        },
        { "id": "Front Construction Lines",
          "type": "path",
          "d": [
            ["M", "pt.frontNeckCenter" ],
            ["L", "pt.t1_frontHemCenter" ],
            ["M", "pt.frontNeckCenter" ],
            ["L", "pt.frontNeckSide" ],
            ["L", "pt.t1_bST" ]
          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"2", "stroke":"#00FF00", "fill":"none" }
        },
        { "id": "Sleeve Construction Lines",
          "type": "path",
          "d": [
            ["M", "pt.f1" ],
            ["L", "pt.f3" ],
            ["M", "pt.f5" ],
            ["L", "pt.f6" ],
            ["L", "pt.f8" ],
            ["L", "pt.f7" ],
            ["L", "pt.f5" ],
            ["L", "pt.f1" ],
            ["L", "pt.f7" ]
          ],
          "drawattr": {},
          "appearanceattr": { "stroke-width":"2", "stroke":"#0000FF", "fill":"none" }
        }
    ],

    "points": {
        "CM": "convertUnit(1, 'cm', window.measurementData.clientdata.measurement_units)",
        "IN": "convertUnit(1, 'in', window.measurementData.clientdata.measurement_units)",
        "seamAllowance": "(5/8)*pt.IN",
        "patternOffset": "1*pt.IN",

        "backNeckCenter": { "x": "1.5*meas.back_hip_width", "y": "2*meas.head_and_neck_length" },
        "backAcrossCenter": "down(pt.backNeckCenter, 0.75*meas.back_highbust_height)",
        "backHighbustCenter": "down(pt.backNeckCenter, 1*meas.back_highbust_height)",
        "backBustCenter": "down(pt.backNeckCenter, 1*meas.back_bust_height)",
        "backWaistCenter": "down(pt.backNeckCenter, 1*meas.back_waist_length)",
        "backNeckSide" : "onCircleAtX(pt.backWaistCenter, 1*meas.back_neck_balance, pt.backNeckCenter.x + 0.5*meas.neck_diameter, 'y1 < y2')" ,
        "backNeckCore" : "up(pt.backNeckCenter, Math.abs(pt.backNeckCenter.y - pt.backNeckSide.y))",
        "t1_bST": "intersectCircles(pt.backNeckSide, 1*meas.shoulder_length, pt.backWaistCenter, 1*meas.back_shoulder_balance, 'y1 > y2')",
        "t2_bST" : "right(pt.t1_bST, 0.1*meas.shoulder_length)",
        "backShoulderTip" : "polar(pt.t2_bST, 0.2*meas.shoulder_length, radians(315))",

        "backArmscye": "right(pt.backAcrossCenter, 0.55*meas.across_back)",
        "backAcrossSide": "right(pt.backAcrossCenter, 0.5*meas.across_back)",
        "t1_bHS" : "right(pt.backHighbustCenter, 0.5*meas.back_bust_width)",
        "backHighbustSide" : "right(pt.backHighbustCenter, 0.55*meas.back_bust_width)",
        "t1_bBS" : "right(pt.backBustCenter, 0.5*meas.back_bust_width)",
        "backBustSide": "right(pt.backBustCenter, 0.55*meas.back_bust_width)",
        "t1_bWS" : "intersectCircles(pt.backHighbustSide, 1.0*meas.side_waist_length, pt.backWaistCenter, 0.5*meas.back_waist_width, 'y1 > y2')",
        "backWaistSide" : "right(pt.t1_bWS, 0.07*dist(pt.backWaistCenter, pt.t1_bWS))",

        "t1_backHemCenter" : "down(pt.backNeckCenter, 1*meas.height - 1*meas.head_and_neck_length)",
        "backHemCenter" : "polar(pt.backWaistCenter, dist(pt.backWaistCenter, pt.t1_backHemCenter), radians(105))",
        "t1_bHipC": "down(pt.backWaistCenter, 1*meas.back_hip_height)",
        "backHipCenter" : "onLineAtLength(pt.backWaistCenter, pt.backHemCenter, 1*meas.back_hip_height)" ,

        "backHemSide" : "polar(pt.t1_bWS, dist(pt.backWaistCenter, pt.t1_backHemCenter), radians(70))",
        "t1_bHipS": "intersectCircles(pt.t1_bHipC, 0.5*meas.back_hip_width, pt.t1_bWS, 1*meas.side_hip_height, 'y1 > y2')",
        "backHipSide" : "onLineAtLength(pt.t1_bWS, pt.backHemSide, 1*meas.side_hip_height)",

        "bNC_in" : "right(pt.backNeckCenter, dist(pt.backNeckCenter, pt.backNeckSide)/2)",
        "bHemC_out" : "polar(pt.backHemCenter, dist(pt.backHemCenter, pt.backHemSide)/3, angleBetween(pt.backHipCenter, pt.backHemCenter) - radians(90) )",
        "bNS_out" : "polar(pt.backNeckSide, dist(pt.backNeckCenter,pt.backNeckSide)/6, angleBetween(pt.backNeckSide, pt.backShoulderTip) + radians(90) )",
        "bSTin" : "polar(pt.backShoulderTip, dist(pt.backShoulderTip, pt.backArmscye)/3, angleBetween(pt.backNeckSide, pt.backShoulderTip) + radians(90) )",
        "bBS_in" : "polar(pt.backBustSide, dist(pt.backBustSide, pt.backWaistSide)/3, angleBetween(pt.backBustSide, pt.backWaistSide))",
        "bBS_out" : "left(pt.backBustSide, dist(pt.backBustSide, pt.backArmscye)/3)",
        "bArm_in"  : "polar(pt.backArmscye, dist(pt.backBustSide,pt.backArmscye)/3.0, 0.5*(angleBetween(pt.bSTin,pt.backArmscye) + angleBetween(pt.backArmscye,pt.bBS_out)))",
        "bArm_out" : "polar(pt.backArmscye, dist(pt.backArmscye,pt.backShoulderTip)/3.0, angleBetween(pt.bArm_in, pt.backArmscye))",

        "bWC_out": "down(pt.backWaistCenter, dist(pt.backHipCenter, pt.backWaistCenter)/6)",
        "bHipC_in" : "polar(pt.backHipCenter, dist(pt.backHipCenter, pt.backWaistCenter)/6, angleBetween(pt.backHemCenter,pt.backHipCenter))",
        "bHipS_out" : "polar(pt.backHipSide, dist(pt.backHipSide, pt.backWaistSide)/3, angleBetween(pt.backHemSide, pt.backHipSide) )",
        "bHemS_in" : "polar(pt.backHemSide, dist(pt.backHemSide, pt.backHemCenter)/3, angleBetween(pt.backHipSide, pt.backHemSide) + radians(90))",
        "bWS_in" : "polar(pt.backWaistSide, dist(pt.backWaistSide, pt.backHipSide)/6, 0.5*(angleBetween(pt.backHipSide, pt.backHemSide) + angleBetween(pt.backBustSide, pt.backWaistSide)))",
        "bWS_out" : "polar(pt.backWaistSide, dist(pt.backBustSide, pt.backWaistSide)/6, angleBetween(pt.bWS_in, pt.backWaistSide))",

        "frontWaistCenter" : "right(pt.backWaistCenter, 1*meas.hip)",
        "frontNeckCenter" : "up(pt.frontWaistCenter, 1*meas.front_waist_length)",
        "frontHighbustCenter": "down(pt.frontNeckCenter, 1*meas.front_highbust_height)",
        "frontHighbustSide": "left(pt.frontNeckCenter, 0.5*meas.front_highbust_width)",
        "frontBustCenter": "down(pt.frontNeckCenter, 1*meas.front_bust_height)",
        "frontBustSide": "left(pt.frontNeckCenter, 0.55*meas.front_bust_width)",
        "frontAcrossCenter": "down(pt.frontNeckCenter, 0.75*meas.front_highbust_height)",
        "frontAcrossSide": "right(pt.frontNeckCenter, 0.5*meas.across_chest)",

        "t1_frontHemCenter" : "down(pt.frontNeckCenter, 1*meas.height - 1*meas.head_and_neck_length)",
        "frontHemCenter" : "polar(pt.frontWaistCenter, dist(pt.frontWaistCenter, pt.t1_frontHemCenter), radians(70))",
        "frontHipCenter" : "polar(pt.frontWaistCenter, 1*meas.side_hip_height, angleBetween(pt.frontWaistCenter, pt.frontHemCenter))",
        "frontNeckSide" : "onCircleAtX(pt.frontWaistCenter, 1*meas.front_neck_balance, pt.frontNeckCenter.x - 0.5*meas.neck_diameter, 'y1 < y2')" ,
        "t1_fST" : "intersectCircles(pt.frontNeckSide, 1*meas.shoulder_length, pt.frontWaistCenter, 1*meas.front_shoulder_balance, 'y1 > y2')",
        "frontArmscye" : { "x": "pt.frontNeckCenter.x - (0.6*meas.across_chest)", "y": "(pt.frontNeckCenter.y + 0.75*meas.front_highbust_height)" },
        "t1_fUS" : { "x": "pt.frontNeckCenter.x - 0.55*meas.front_bust_width", "y": "(pt.frontNeckCenter.y + 1.0*meas.front_highbust_height)" },
        "temp_b9" : { "x": "pt.t1_fUS.x", "y" : "pt.frontWaistCenter.y" },
        "frontUnderarm": { "x": "pt.t1_fUS.x", "y": "(pt.t1_fST.y + 1.0*meas.front_bust_height)" },
        "b9" : "intersectCircles(pt.t1_fUS, 1.0*meas.side_waist_length, pt.frontWaistCenter, 0.5*meas.front_waist_width, 'y1 > y2')",
        "b11" : "polar(pt.temp_b9, dist(pt.frontWaistCenter, pt.t1_frontHemCenter), radians(110))",
        "b10" : "onLineAtLength(pt.b9, pt.b11, 1*meas.side_hip_height)",
        "b12" : "left(pt.b9, 0.02*dist(pt.frontWaistCenter, pt.b9))",
        "b13" : "down(pt.frontNeckCenter, 0.25*meas.front_highbust_height)",
        "b14" : "left(pt.frontWaistCenter, 0.6*dist(pt.frontNeckCenter, pt.t1_fST))",
        "b15" : "down(pt.b14, 0.25*dist(pt.b9, pt.b10))",
        "b17" : { "x": "pt.b15.x", "y": "pt.b15.y + 1.15*meas.hand_length" },
        "temp_b18" : "left(pt.b17, 0.5*dist(pt.b12, pt.b10))",
        "b18" : "intersectLines(pt.b17, pt.temp_b18, pt.b10, pt.b11)",
        "b19" : { "x": "pt.frontNeckCenter.x - 0.75*(pt.frontNeckCenter.x - pt.frontArmscye.x)", "y": "pt.frontUnderarm.y" },
        "b20_temp" : "polar(pt.t1_fST, 0.2*meas.shoulder_length, radians(225))",
        "b20" : "up(pt.b20_temp, 0.2*meas.shoulder_length)",
        "fNC_in" : "left(pt.frontNeckCenter, dist(pt.frontNeckCenter, pt.frontNeckSide)/2)",
        "fWC_out" : "down(pt.frontWaistCenter, dist(pt.frontWaistCenter, pt.frontHipCenter)/3)",
        "b3out" : "polar(pt.frontHemCenter, dist(pt.frontHemCenter, pt.b11)/3, angleBetween(pt.frontHipCenter, pt.frontHemCenter) + radians(90) )",

        "fNS_out" : "polar(pt.frontNeckSide, dist(pt.frontNeckCenter,pt.frontNeckSide)/3, angleBetween(pt.frontNeckSide, pt.b20) - radians(90) )",
        "b20in" : "polar(pt.b20, dist(pt.b20, pt.frontArmscye)/3, angleBetween(pt.frontNeckSide, pt.b20) - radians(90) )",
        "fUnd_in" : "polar(pt.frontUnderarm, dist(pt.frontUnderarm, pt.b12)/3, angleBetween(pt.frontUnderarm, pt.b12))",
        "fUnd_out" : "right(pt.frontUnderarm, dist(pt.frontUnderarm, pt.frontArmscye)/2.0)",
        "fArm_in"  : "polar(pt.frontArmscye, dist(pt.frontUnderarm,pt.frontArmscye)/3.0, 0.5*(angleBetween(pt.b20in,pt.frontArmscye) + angleBetween(pt.frontArmscye,pt.fUnd_out)))",
        "fArm_out"  : "polar(pt.frontArmscye, dist(pt.frontArmscye,pt.b20)/3.0, angleBetween(pt.fArm_in, pt.frontArmscye))",
        "b10out" : "polar(pt.b10, dist(pt.b10, pt.b12)/3, angleBetween(pt.b11, pt.b10))",
        "b11in" : "polar(pt.b11, dist(pt.b11, pt.frontHemCenter)/3, angleBetween(pt.b10, pt.b11) - radians(90))",
        "b12in" : "polar(pt.b12, dist(pt.b12, pt.b10)/6, angleBetween(pt.frontUnderarm, pt.b10))",
        "b12out" : "polar(pt.b12, dist(pt.frontUnderarm, pt.b12)/3, angleBetween(pt.b10, pt.frontUnderarm))",
        "b13out" : "polar(pt.b13, 0.3*dist(pt.frontNeckCenter, pt.frontUnderarm),1.1*angleBetween(pt.b13, pt.b19))",
        "b14in" : "up(pt.b14, 0.3*dist(pt.b14, pt.frontArmscye))",
        "b14out" : "down(pt.b14, 0.3*dist(pt.b14, pt.b15))",
        "b15in" : "polar(pt.b15, 0.3*dist(pt.b14, pt.b15), angleBetween(pt.b15, pt.b14out))",
        "b19in" : "up(pt.b19, 0.5*dist(pt.b19, pt.frontArmscye))",
        "b19out" : "down(pt.b19, 0.3*dist(pt.b19, pt.b14))",


        "c1" : "right(pt.b13, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c2" : "right(pt.frontWaistCenter, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c3" : "right(pt.frontHemCenter, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c3out" : "right(pt.b3out, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c4in" : "right(pt.b11in, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c4" : "right(pt.b11, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c5" : "right(pt.b10, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c6" : "right(pt.b15, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c6out" : "right(pt.b15in, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c7in" : "right(pt.b14out, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c7" : "right(pt.b14, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c7out" : "right(pt.b14in, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c8in" : "right(pt.b19out, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c8" : "right(pt.b19, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c8out" : "right(pt.b19in, 2*dist(pt.frontArmscye, pt.frontNeckSide))",
        "c1in" : "right(pt.b13out, 2*dist(pt.frontArmscye, pt.frontNeckSide))",

        "d1" : { "x": "pt.frontNeckCenter.x + 2*pt.patternOffset", "y": "pt.frontNeckCenter.y - 2*pt.patternOffset" },
        "d2" : "right(pt.d1, 0.80*(curveLength(pt.backNeckSide,pt.bNS_out,pt.bNC_in,pt.backNeckCenter) + curveLength(pt.frontNeckSide,pt.fNS_out,pt.fNC_in,pt.frontNeckCenter)))",
        "d3" : "up(pt.d1, 1.3*meas.head_and_neck_length)",
        "d4" : "up(pt.d2, 1.4*meas.head_and_neck_length)",
        "d5" : "midPoint(pt.d1, pt.d3)",
        "d6" : "left(pt.d5, 0.15*meas.head_and_neck_length)",
        "d7" : "midPoint(pt.d3, pt.d4)",
        "d8" : "down(pt.d4, 0.75*dist(pt.d1, pt.d3))",
        "d9" : {"x":"pt.d2.x + 0.25*dist(pt.d1, pt.d2)", "y": "pt.d2.y"},
        "d10" : "polar(pt.d1, dist(pt.d1, pt.d2), 0.5*angleBetween(pt.frontNeckSide, pt.frontNeckCenter))",
        "d1out" : "up(pt.d1, dist(pt.d1, pt.d6)/6)",
        "d6in" : "down(pt.d6, dist(pt.d6, pt.d1)/3)",
        "d6out" : "up(pt.d6, dist(pt.d6, pt.d7)/3)",
        "d7in" : "left(pt.d7, dist(pt.d6, pt.d7)/3)",
        "d8out" : "down(pt.d8, dist(pt.d8, pt.d9)/3)",
        "d9in" : "polar(pt.d9, dist(pt.d8, pt.d9)/3, angleBetween(pt.d9, pt.d10) + radians(90))",

        "e1" : { "x" : "pt.frontArmscye.x", "y" : "pt.d5.y" },
        "e2" : "up(pt.e1, dist(pt.d1, pt.d2)/3)",
        "e3" : "left(pt.e2, curveLength(pt.d1, pt.d1out, pt.d6in, pt.d6) + curveLength(pt.d6, pt.d6out, pt.d7in, pt.d7) + dist(pt.d7, pt.d4))",
        "e4" : "down(pt.e3, dist(pt.e1, pt.e2))",

        "f1": { "x" : "pt.backHemCenter.x - dist(pt.backNeckSide, pt.t1_bST)" , "y" : "pt.e3.y"},
        "f2": "down(pt.f1, 0.3*( curveLength(pt.backBustSide, pt.bBS_out, pt.bArm_in, pt.backArmscye) + curveLength(pt.backArmscye, pt.bArm_out, pt.bSTin, pt.backShoulderTip) + curveLength(pt.frontUnderarm, pt.fUnd_out, pt.fArm_in, pt.frontArmscye) + curveLength(pt.frontArmscye, pt.fArm_out, pt.b20in, pt.b20) ) )",
        "f3": "down(pt.f1, 1.02*meas.overarm_length)",
        "f4": "midPoint(pt.f2, pt.f3)",
        "f5": "onCircleAtY(pt.f1, curveLength(pt.backBustSide, pt.bBS_out, pt.bArm_in, pt.backArmscye) + curveLength(pt.backArmscye, pt.bArm_out, pt.bSTin, pt.backShoulderTip), pt.f2.y, 'x1 < x2')",
        "f6": "down(pt.f5, dist(pt.f2, pt.f3))",
        "f7": "onCircleAtY(pt.f1, curveLength(pt.frontUnderarm, pt.fUnd_out, pt.fArm_in, pt.frontArmscye) + curveLength(pt.frontArmscye, pt.fArm_out, pt.b20in, pt.b20), pt.f2.y, 'x1 > x2')",
        "f8": "down(pt.f7, dist(pt.f2, pt.f3))",
        "f9" : "right(pt.f6, 0.25*dist(pt.f6, pt.f3))",
        "f10" : "left(pt.f8, 0.25*dist(pt.f8, pt.f3))",
        "f11" : "onLineAtLength(pt.f5, pt.f9, dist(pt.f5, pt.f9)/4)",
        "f12" : "onLineAtLength(pt.f7, pt.f10, dist(pt.f7, pt.f10)/4)",
        "f13" : "polar(pt.f6, 3*pt.CM, radians(135))",
        "f14" : "polar(pt.f8, 3*pt.CM, radians(45))",
        "f1in" : "left(pt.f1, dist(pt.f5, pt.f1)/3)",
        "f1out" : "right(pt.f1, dist(pt.f1, pt.f7)/3)",
        "f3in" : "right(pt.f3, dist(pt.f3, pt.f14)/3)",
        "f3out" : "left(pt.f3, dist(pt.f3, pt.f13)/3)",
        "f5out" : "right(pt.f5, dist(pt.f5, pt.f1)/5)",
        "f7in" : "left(pt.f7, dist(pt.f1, pt.f7)/4)",
        "f11in" : "polar(pt.f11, dist(pt.f11, pt.f13)/6, angleBetween(pt.f5, pt.f11))",
        "f12out" : "polar(pt.f12, dist(pt.f12, pt.f8)/6, angleBetween(pt.f7, pt.f12))",
        "f13in" : "polar(pt.f13, dist(pt.f13, pt.f3)/3, angleBetween(pt.f13, pt.f3out))",
        "f13out" : "polar(pt.f13, dist(pt.f11, pt.f13)/3, angleBetween(pt.f13, pt.f11in))",
        "f14in" : "polar(pt.f14, dist(pt.f12, pt.f14)/3, angleBetween(pt.f14, pt.f12out))",
        "f14out" : "polar(pt.f14, dist(pt.f14, pt.f3)/3, angleBetween(pt.f14, pt.f3in))",
        "g1" : "down(pt.b15, dist(pt.b15, pt.b17) + 20*pt.CM)",
        "g2" : "down(pt.b17, dist(pt.b15, pt.b17) + 20*pt.CM)",
        "g3" : "down(pt.b18, dist(pt.b15, pt.b17) + 20*pt.CM)",
        "g4" : "down(pt.b10out, dist(pt.b15, pt.b17) + 20*pt.CM)",
        "h1" : "up(pt.g1, 6*pt.CM)",
        "h2" : "polar(pt.h1, 5*pt.CM, angleBetween(pt.g1, pt.g4) + radians(90))",
        "h3" : "polar(pt.h2, dist(pt.g1, pt.g4), angleBetween(pt.g1, pt.g4))",
        "h4" : "polar(pt.h3, 5*pt.CM, angleBetween(pt.h2, pt.h1))"
    }
  }
}
