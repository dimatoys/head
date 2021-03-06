from math import sin, cos, atan, pi, acos, asin
from PIL import Image
import json

import numpy as np
import datetime

import sys
import os
sys.path.append('.')

from Geometry import MinResolve, ResolveSymmetry, SampleImage, TModelPoly, TPolyRegression, TLearning

pictures = {"3900-2500.jpg": {  "A": 3900,
                                "B": 2500,
                                "img": [(16, 120),
                                        (6, 209),
                                        (157, 121),
                                        (158, 209),
                                        (296, 123),
                                        (305, 208)],
                                "x": 50,
                                "y": [180, 210]},
            "3700-2500.jpg": {  "A": 3700,
                                "B": 2500,
                                "img": [(33, 54),
                                        (29, 131),
                                        (25, 212),
                                        (160, 56),
                                        (160, 131),
                                        (160, 212),
                                        (285, 57),
                                        (289, 132),
                                        (292, 210)],
                                "x": 50,
                                "y": [180, 210, 240]},
            "3500-2500.jpg": {  "A": 3500,
                                "B": 2500,
                                "img": [(17, 44),
                                        (16, 116),
                                        (16, 212),
                                        (161, 47),
                                        (160, 118),
                                        (159, 214),
                                        (301, 49),
                                        (301, 120),
                                        (299, 213)],
                                "x": 60,
                                "y": [200, 230 ,270]},
            "3300-2500.jpg": {  "A": 3300,
                                "B": 2500,
                                "img": [(3, 18),
                                        (7, 129),
                                        (12, 232),
                                        (160, 20),
                                        (158, 130),
                                        (157, 234),
                                        (314, 23),
                                        (307, 131),
                                        (300, 232)],
                                "x": 70,
                                "y": [210, 260, 310]},
            "3100-2500.jpg": {  "A": 3100,
                                "B": 2500,
                                "img": [(13, 15),
                                        (21, 118),
                                        (30, 224),
                                        (160, 17),
                                        (159, 120),
                                        (159, 225),
                                        (305, 20),
                                        (295, 120),
                                        (283, 225)],
                                "x": 70,
                                "y": [230, 280, 340]},
            "2800-2500.jpg": {  "A": 2800,
                                "B": 2500,
                                "img": [(17, 20),
                                        (32, 120),
                                        (50, 234),
                                        (164, 21),
                                        (162, 121),
                                        (160, 234),
                                        (308, 24),
                                        (290, 123),
                                        (268, 234)],
                                "x": 80,
                                "y": [270, 330, 420]},
            "2500-2500.jpg": {  "A": 2500,
                                "B": 2500,
                                "img": [(48, 6),
                                        (68, 127),
                                        (85, 230),
                                        (163, 8),
                                        (160, 128),
                                        (157, 231),
                                        (276, 10),
                                        (251, 130),
                                        (229, 231)],
                                "x": 70,
                                "y": [300, 390, 510]},
            "2300-2500.jpg": {  "A": 2300,
                                "B": 2500,
                                "img": [(59, 7),
                                        (78, 112),
                                        (90, 181),
                                        (159, 8),
                                        (160, 113),
                                        (160, 182),
                                        (265, 11),
                                        (241, 115),
                                        (225, 182)],
                                "x": 70,
                                "y": [330, 420, 510]},
            "2100-2500.jpg": {  "A": 2100,
                                "B": 2500,
                                "img": [(69, 8),
                                        (83, 83),
                                        (94, 141),
                                        (161, 9),
                                        (160, 84),
                                        (160, 142),
                                        (256, 13),
                                        (238, 85),
                                        (223, 142)],
                                "x": 70,
                                "y": [360, 430, 510]}}                 

spictures = {"3500-2000.jpg":{  "A": 3500,
                                "B": 2000,
                                "real":[(140, 180),
                                        (140, 240),
                                        (60, 180),
                                        (90, 270)],
                                "img":[(105, 110),
                                       (180, 231),
                                       (265, 11),
                                       (315, 227)]},
             "3500-3000.jpg":{  "A": 3500,
                                "B": 3000,
                                "real":[(-140, 180),
                                        (-140, 240),
                                        (-60, 180),
                                        (-90, 270)],
                                "img":[(221, 114),
                                       (146 ,233),
                                       (61, 12),
                                       (7, 231)]},
             "3500-2400.jpg":{  "A": 3500,
                                "B": 2400,
                                "real":[(-40, 190),
                                        (-30, 280),
                                        (80, 180),
                                        (90, 270)],
                                "img":[(305, 12),
                                       (304 ,223),
                                       (20, 16),
                                       (20, 233)]},
             "3500-2600.jpg":{  "A": 3500,
                                "B": 2600,
                                "real":[(40, 190),
                                        (30, 280),
                                        (-80, 180),
                                        (-90, 270)],
                                "img":[(18, 8),
                                       (14, 225),
                                       (301, 21),
                                       (299, 232)]},
             "3500-2100.jpg":{  "A": 3500,
                                "B": 2100,
                                "real":[(140, 180),
                                        (50, 180),
                                        (140, 240),
                                        (60, 270)],
                                "img":[(43, 99),
                                       (237, 9),
                                       (105, 229),
                                       (305, 209)]},
             "3500-2900.jpg":{  "A": 3500,
                                "B": 2900,
                                "real":[(-140, 180),
                                        (-50, 180),
                                        (-140, 240),
                                        (-60, 270)],
                                "img":[(283, 103),
                                       (92, 10),
                                       (223, 230),
                                       (20, 214)]}}
"""
             real       2000        3000
             (140, 180)    (105, 110)    (221, 114)
             (140, 240)   (180, 231)     (146 ,233)
             (60, 180)    (265, 11)     (61, 12)
             (90, 270)    (315, 227)     (7, 231)
             
             real       2400        2600
             (-40, 190)   (305,12)      (18,8)
             (-30, 280)   (304,223)     (14,225)
             (80,180)     (20,16)       (301,21)
             (90,270)     (20,233)      (299,232)

             real       2100        2900
             (140,180)    (43,99)       (283,103)
             (50,180)     (237,9)       (92,10)
             (140,240)    (105,229)     (223,230)
             (60,270)     (305,209)     (20,214)
"""

gripper = [{"view": 3643, # y = 230
            "grab": [{"GR": 0,      "G": 2500,  "A": 4670},
                     {"GR": 2500,   "G": 4452,  "A": 3149},
                     {"GR": 5000,   "G": 4738,  "A": 2862}]},
            {"view": 3885, # y = 204.6
            "grab": [{"GR": 0,      "G": 3941,  "A": 3864},
                     {"GR": 2500,   "G": 4764,  "A": 3111},
                     {"GR": 5000,   "G": 5000,  "A": 2849}]},
            {"view": 4500,
            "grab": [{"GR": 0,      "G": 4370,  "A": 4058},
                     {"GR": 2200,   "G": 5000,  "A": 3479}]}]
      
class TTest2(MinResolve):
    def Target(self, x):
        return (x[0] - 3) * (x[0] - 3) + (x[1] + 2) *(x[1] + 2)

class PictureTransform(MinResolve):
    
    def __init__(self, points):
        self.MU = points[0]
        self.MC = points[1]
        self.MD = points[2]
        self.CU = points[3]
        self.CC = points[4]
        self.CD = points[5]
        self.PU = points[6]
        self.PC = points[7]
        self.PD = points[8]
    
    def Transform(self, x, y, x0, y0, a):
        dx = x - x0
        dy = y - y0
        s = sin(a)
        c = cos(a)
        return (dx * c - dy * s + x0,
                dx * s + dy * c + y0)
                
    def Target(self, x):
        x0 = x[0]
        y0 = x[1]
        a = x[2]
        (mux, muy) = self.Transform(self.MU[0], self.MU[1], x0, y0 , a)
        (cux, cuy) = self.Transform(self.CU[0], self.CU[1], x0, y0 , a)
        (pux, puy) = self.Transform(self.PU[0], self.PU[1], x0, y0 , a)
        (mcx, mcy) = self.Transform(self.MC[0], self.MC[1], x0, y0 , a)
        (ccx, ccy) = self.Transform(self.CC[0], self.CC[1], x0, y0 , a)
        (pcx, pcy) = self.Transform(self.PC[0], self.PC[1], x0, y0 , a)
        (mdx, mdy) = self.Transform(self.MD[0], self.MD[1], x0, y0 , a)
        (cdx, cdy) = self.Transform(self.CD[0], self.CD[1], x0, y0 , a)
        (pdx, pdy) = self.Transform(self.PD[0], self.PD[1], x0, y0 , a)
    
        t1 = ccx - cux
        t2 = ccx - cdx
        t3 = muy - puy
        t4 = mcy - pcy
        t5 = mdy - pdy
        t6 =  2 * cux - mux - pux
        t7 =  2 * ccx - mcx - pcx
        t8 =  2 * cdx - mdx - pdx
        
        return t1 * t1 + t2 * t2 + t3 * t3 + t4 * t4 + t5 * t5 + t6 * t6 + t7 * t7 + t8 * t8

    def ResolveSymmetry(self, x0, y0, a0, sx, sy, sa):
        self.Reset([x0, y0, a0], [sx, sy, sa])
        (xmin, self.Min, self.Min0) = self.ResolveSimple()
        self.X0 = xmin[0]
        self.Y0 = xmin[1]
        self.A = xmin[2]
        return (xmin, self.Min, self.Min0)
    
    def TransformFrom(self, x):
        return self.Transform(x[0], x[1], self.X0, self.Y0, self.A)
    
    def TransformFromImage(self, name):
        img = Image.open(name)
        dst = Image.new(img.mode, img.size)
    
        for y in range(dst.height):
            for x in range(dst.width):
                (nx, ny) = self.Transform(x, y, self.X0, self.Y0, -self.A)
                nx = int(nx)
                ny = int(ny)
                if nx >= 0 and ny >= 0 and nx < img.width and ny < img.height:
                    dst.putpixel((x, y), img.getpixel((nx, ny)))
        return dst
        
    
def Test2():
    t2 = TTest2()
    t2.Reset([0, 0], [0.1, 0.1])
    print t2.ResolveSimple()

def Im1():
    pt = PictureTransform([(17, 44),
                           (16, 116),
                           (16, 212),
                           (161, 47),
                           (160, 118),
                           (159, 214),
                           (301, 49),
                           (301, 120),
                           (299, 213)])
    pt.Reset([160.0, 118.0, 0], [.5, .5, 0.0001])
    print pt.ResolveSimple()

def DrawPointer(img, xy, color):
    (x,y) = xy
    x = int(x)
    y = int(y)
    if 0 <= x < img.width and 0 <= y < img.height:
        img.putpixel((x, y), color)
    if 0 <= (x - 1) < img.width and 0 <= y < img.height:
        img.putpixel((x - 1, y), color)
    if 0 <= (x + 1) < img.width and 0 <= y < img.height:
        img.putpixel((x + 1, y), color)
    if 0 <= x < img.width and 0 <= (y - 1) < img.height:
        img.putpixel((x, y - 1), color)
    if 0 <= x < img.width and 0 <= (y + 1) < img.height:
        img.putpixel((x, y + 1), color)
    

def Draw1(file):
    global pictures
    img = Image.open('VideoTest/%s' % file)
    orig_points = (255, 0, 0)
    for xy in pictures[file]["img"]:
        DrawPointer(img, xy, orig_points)
    img.save('img.png', 'PNG')

def DrawTurn(file):
    global pictures

    pt = PictureTransform(pictures[file]["img"])
    print pt.ResolveSymmetry(160.0, 118.0, 0, .5, .5, 0.0001)
    
    img = Image.open('VideoTest/%s' % file)
    orig_points = (255, 0, 0)
    tr_points = (0, 255, 0)
    center_point = (0, 0, 255)
    for xy in pictures[file]["img"]:
        DrawPointer(img, xy, orig_points)
        xyt = pt.Transform(xy[0], xy[1], pt.X0, pt.Y0, pt.A)
        DrawPointer(img, xyt, tr_points)
    DrawPointer(img, (pt.X0, pt.Y0), center_point)
    img.save('img.png', 'PNG')

def CountFit(fit, x):
    result = 0
    for a in fit:
        result = result * x + a
    return result

def DrawTurn2(file):
    global pictures

    pic = pictures[file]
    pt = PictureTransform(pic["img"])
    print pt.ResolveSymmetry(160.0, 118.0, 0, .5, .5, 0.0001)
    dst = pt.TransformFromImage('VideoTest/%s' % file)
    
    tr_points = (0, 255, 0)
    center_point = (0, 0, 255)
    
    for cp in pic["img"]:
        DrawPointer(dst, pt.TransformFrom(cp), tr_points)
    
    
    (cux, cuy) = pt.TransformFrom(pt.CU)
    (ccx, ccy) = pt.TransformFrom(pt.CC)
    (cdx, cdy) = pt.TransformFrom(pt.CD)

    fit = np.polyfit(np.array(pic["y"]), np.array([cuy, ccy, cdy]), 2)
    print fit
    
    for y in range(pic["y"][0], pic["y"][-1], 10):
        py = CountFit(fit, y)
        print y, py
        DrawPointer(dst, (ccx, py), tr_points)

    DrawPointer(dst, (pt.X0, pt.Y0), center_point)
    dst.save('img.png', 'PNG')

def modelV(p, x):
    a, b, c = p
    return (a * x + b) * x + c

def modelXY2(p, v):
    a1, a2, a3, a4, a5, a6 = p
    x, y = v
    return a1 + a2 * x + a3 * y + a4 * x * x + a5 * y * y + a6 * x * y

def DrawTurn3(file):

    from kapteyn import kmpfit 
    global pictures

    pic = pictures[file]
    pt = PictureTransform(pic["img"])
    print pt.ResolveSymmetry(160.0, 118.0, 0, .5, .5, 0.0001)
    dst = pt.TransformFromImage('VideoTest/%s' % file)
    
    tr_points = (0, 255, 0)
    center_point = (0, 0, 255)
    
    for cp in pic["img"]:
        DrawPointer(dst, pt.TransformFrom(cp), tr_points)
    
    (cux, cuy) = pt.TransformFrom(pt.CU)
    (ccx, ccy) = pt.TransformFrom(pt.CC)
    (cdx, cdy) = pt.TransformFrom(pt.CD)

    p = (1.0, 1.0, 1.0)
    fit = kmpfit.simplefit(modelV, p, pic["y"], [cuy, ccy, cdy])
    print fit.params

    for y in range(pic["y"][0], pic["y"][-1], 10):
        py = modelV(fit.params, y)
        print y, py
        DrawPointer(dst, (ccx, py), tr_points)

    DrawPointer(dst, (pt.X0, pt.Y0), center_point)
    dst.save('img2.png', 'PNG')

def TestLinarg():
    # https://en.wikipedia.org/wiki/Polynomial_regression
    from numpy.linalg import inv
    import numpy as np
    a = np.array([[1., 2.], [3., 4.]])
    ainv = inv(a)
    print ainv
    print np.dot(a, ainv)
    
def TestLinarg():
    from numpy.linalg import inv
    import numpy as np

    global pictures

    pic = pictures[file]
    pt = PictureTransform(pic["img"])
    print pt.ResolveSymmetry(160.0, 118.0, 0, .5, .5, 0.0001)

    (cux, cuy) = pt.TransformFrom(pt.CU)
    (ccx, ccy) = pt.TransformFrom(pt.CC)
    (cdx, cdy) = pt.TransformFrom(pt.CD)

    fit = np.polyfit(np.array(pic["y"]), np.array([cuy, ccy, cdy]), 2)
    print fit

    T = [[1.0, float(pic["y"][0]), float(pic["y"][0]) * float(pic["y"][0])],
         [1.0, float(pic["y"][1]), float(pic["y"][1]) * float(pic["y"][1])],
         [1.0, float(pic["y"][2]), float(pic["y"][2]) * float(pic["y"][2])]]
    yv = [[cuy], [ccy], [cdy]]
    
    T = np.array(T)
    TT = T.transpose()
    r = np.dot(np.dot(inv(np.dot(TT, T)), TT), np.array(yv))
    print yv
    print np.dot(T, r)
    
    fitt = [[fit[2]], [fit[1]], [fit[0]]]
    print np.dot(T, np.array(fitt))

def modelPoly(i, x):
    if i == 0:
        return 1.0
    if len(x) == 1:
        return modelPoly(i - 1, x) * float(x[0])
    if i < 3:
        return modelPoly(1, [x[i - 1]])
    if i < 6:
        return modelPoly(5 - i, x[0:1]) * modelPoly(i - 3, x[1:2])
    
  
def PolyTest():
    p = TModelPoly([1, 2, 3, 4])
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()    
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()
    p.Next()    

def DrawTurn4(file):
    from numpy.linalg import inv
    import numpy as np

    global pictures

    pic = pictures[file]
    pt = PictureTransform(pic["img"])
    print pt.ResolveSymmetry(160.0, 118.0, 0, .5, .5, 0.0001)
    dst = pt.TransformFromImage('VideoTest/%s' % file)
    
    tr_points = (0, 255, 0)
    center_point = (0, 0, 255)
    
    for cp in pic["img"]:
        DrawPointer(dst, pt.TransformFrom(cp), tr_points)

    (cux, cuy) = pt.TransformFrom(pt.CU)
    (ccx, ccy) = pt.TransformFrom(pt.CC)
    (cdx, cdy) = pt.TransformFrom(pt.CD)

    n = 3
    T = []
    for y in pic["y"]:
        tr = []
        for f in range(3):
            tr.append(modelPoly(f, y))
        T.append(tr)
    
    yv = [[cuy], [ccy], [cdy]]
    
    T = np.array(T)
    TT = T.transpose()
    r = np.dot(np.dot(inv(np.dot(TT, T)), TT), np.array(yv))
    print np.dot(T, r)
    
    for y in range(pic["y"][0], pic["y"][-1], 10):
        py = 0
        for i in range(n):
            py = py + r[i][0] * modelPoly(i, y)
        print y, py
        DrawPointer(dst, (ccx, py), tr_points)

    
    DrawPointer(dst, (pt.X0, pt.Y0), center_point)
    dst.save('img2.png', 'PNG')

def MakeReal():
    global pictures
    for file,data in pictures.items():
        data["real"] = []
        for x in [data["x"], 0, -data["x"]]:
            for y in data["y"]:
                data["real"].append((x, y))

def DrawTurn5(file):
    from numpy.linalg import inv
    import numpy as np

    global pictures

    MakeReal()

    pic = pictures[file]
    pt = PictureTransform(pic["img"])
    print pt.ResolveSymmetry(160.0, 118.0, 0, .5, .5, 0.0001)
    dst = pt.TransformFromImage('VideoTest/%s' % file)
    
    tr_points = (0, 255, 0)
    center_point = (0, 0, 255)
    
    for cp in pic["img"]:
        DrawPointer(dst, pt.TransformFrom(cp), tr_points)

    T = []
    yx = []
    yy = []
    s = 2
    for i in range(len(pic["img"])):
        tr = []
        pm = TModelPoly(pic["real"][i])
        while pm.S <= s:
            tr.append(pm.Next())
        T.append(tr)
        (x, y) = pt.TransformFrom(pic["img"][i])
        yx.append([x])
        yy.append([y])
    
    T = np.array(T)
    TT = T.transpose()
    r = np.dot(inv(np.dot(TT, T)), TT)
    rx = np.dot(r, np.array(yx))
    ry = np.dot(r, np.array(yy))
    
    for y in range(pic["y"][0], pic["y"][-1], 10):
        for x in range(-pic["x"], pic["x"], 10):
            px = 0
            py = 0
            pm = TModelPoly((x,y))
            i = 0
            while pm.S <= s:
                v = pm.Next()
                px = px + rx[i][0] * v
                py = py + ry[i][0] * v
                i = i + 1
            DrawPointer(dst, (px, py), tr_points)

    
    DrawPointer(dst, (pt.X0, pt.Y0), center_point)
    dst.save('img2.png', 'PNG')

def DrawTurn6(file):
    global pictures

    MakeReal()

    pic = pictures[file]
    pt = PictureTransform(pic["img"])
    print pt.ResolveSymmetry(160.0, 118.0, 0, .5, .5, 0.0001)
    dst = pt.TransformFromImage('VideoTest/%s' % file)
    
    tr_points = (255, 0, 0)
    pr_points = (0, 255, 0)
    center_point = (0, 0, 255)
    
    pic["corr"] = []
    for cp in pic["img"]:
        tcp = pt.TransformFrom(cp)
        pic["corr"].append(tcp)
        DrawPointer(dst, tcp, tr_points)

    pr = TPolyRegression(2)
    pr.Learn(pic["real"], pic["corr"])
    
    for y in range(pic["y"][0], pic["y"][-1], 10):
        for x in range(-pic["x"], pic["x"], 10):
            DrawPointer(dst, pr.GetValue((x, y)), pr_points)

    DrawPointer(dst, (pt.X0, pt.Y0), center_point)
    dst.save('img2.png', 'PNG')

def DrawTurn7():
    global pictures

    file = "2100-2500.jpg"

    files = pictures.keys()
    files.remove("3900-2500.jpg")
    files.remove(file)

    x = []
    y = []
    for f in files:
        pic = SampleImage(f, pictures[f])
        for i in range(pic.N):
            (rx, ry) = pic.GetReal(i)
            x.append((rx, ry, pic.A))
            y.append(pic.Img[i])
    
    pr = TPolyRegression(3)
    pr.Learn(x, y)
    
    img = SampleImage(file, pictures[file])
    
    tr_points = (255, 0, 0)
    pr_points = (0, 255, 0)
    
    for cp in img.Img:
        img.DrawPointer(cp, tr_points)

    for y in range(img.MinY, img.MaxY + 1, 10):
        for x in range(img.MinX, img.MaxX + 1, 10):
            p = pr.GetValue((x, y, img.A))
            img.DrawPointer(p, pr_points)

    img.Save('img03.png', 'PNG')

def DrawTurn8(file):
    global pictures
    pic = SampleImage(file, pictures[file])
    width = pic.GetImage().width
    height = pic.GetImage().height
    pr = TPolyRegression(2)
    pr.Learn(pic.Img, pic.GetReal())
    
    points = []
    for i in range(len(pic.Img)):
        (x, y) = pic.Img[i]
        points.append((pr.GetValue((x, y)), pr.GetValue((width - x , y))))
        
    rs = ResolveSimmetry(points)
    print rs.Resolve(width/ 2, height / 2, 0, 0, 0.001, 0.001, 0.00001, 0.001)
    
    orig = []
    for i in range(len(pic.Img)):
        (x, y) = pic.Img[i]
        (rx, ry) = pic.GetReal(i)
        (lx, ly) = pr.GetValue((x, y))
        (sx, sy) = pr.GetValue((width - x , y))
        (ox, oy) = rs.TransformOpt((rx,ry))
        orig.append((ox, oy))
        
        print "img(%d, %d)\treal=(%d, %d)\tlearn=(%f, %f)\tsymmetry=(%f, %f) orig=(%f, %f)" % (x, y, rx, ry, lx, ly, sx, sy, ox, oy)
    
    pr2 = TPolyRegression(2)
    pr2.Learn(orig, pic.Img)
    
    tr_points = (255, 0, 0)
    pr_points = (0, 255, 0)
    
    for cp in pic.Img:
        pic.DrawPointer(cp, tr_points)

    for y in range(pic.MinY, pic.MaxY + 1, 10):
        for x in range(pic.MinX, pic.MaxX + 1, 10):
            p = pr2.GetValue((x, y))
            pic.DrawPointer(p, pr_points)

    pic.Save('img2.png', 'PNG')

def DrawTurn9():
    global pictures

    file = "2100-2500.jpg"

    files = pictures.keys()
    files.remove("3900-2500.jpg")
    files.remove(file)

    x = []
    y = []
    for f in files:
        pic = SampleImage(f, pictures[f])
        rs = pic.ResolveSymmetry()
        for i in range(pic.N):
            (ox, oy) = rs.TransformOpt(pic.GetReal(i))
            x.append((ox, oy, pic.A))
            y.append(pic.Img[i])
    
    pr = TPolyRegression(3)
    pr.Learn(x, y)
    
    img = SampleImage(file, pictures[file])
    
    tr_points = (255, 0, 0)
    pr_points = (0, 255, 0)
    
    for cp in img.Img:
        img.DrawPointer(cp, tr_points)

    for y in range(img.MinY, img.MaxY + 1, 10):
        for x in range(img.MinX, img.MaxX + 1, 10):
            p = pr.GetValue((x, y, img.A))
            img.DrawPointer(p, pr_points)

    img.Save('img3.png', 'PNG')

def TestEq():

    f = lambda x: 3 * x * x * x * x * x - x * x * x * x  + 2 * x * x * x + 4 * x * x + 3* x + 5

    x = []
    y = []
    for i in range(6):
        x.append([i])
        y.append([f(i)])

    pr = TPolyRegression(len(x) - 1)
    pr.Learn(x, y)
    
    print pr.R
    
def LearnA():
    global pictures

    files = pictures.keys()
    files.remove("3900-2500.jpg")

    #y0 = -15.0297784555
    y0 = 0

    x = []
    y = []
    A = []
    for f in files:
        pic = SampleImage(f, pictures[f])
        rs = pic.ResolveSymmetry()
        for i in range(pic.N):
            x.append((pic.Img[i][0], pic.Img[i][1], pic.A))
            (tx, ty) = rs.TransformOpt(pic.GetReal(i))
            y.append((tx, ty - y0))
        A.append(pic.A)
    
    pr = TPolyRegression(3)
    pr.Learn(x, y)
    print "D", pr.R

    ax = []
    ay = []
    for a in A:
        (ox, oy) = pr.GetValue((160, 120, a))
        ax.append([oy])
        ay.append([a])
        
    pra = TPolyRegression(pr.S)
    pra.Learn(ax, ay)
    
    print "A", pra.R
    
    for f in files:
        d = pictures[f]["y"][1] - y0
        a = pictures[f]["A"]
        print a, d, pra.GetValue([d])
        
def TestA():
    D = TPolyRegression(3) 
    D.R = [[  4.43813268e+02,   1.05282991e+03],
        [ -2.16923364e-01,  -5.88883706e-01],
        [  9.06797661e-01,   3.93421281e+00],
        [ -2.92477465e+00,   5.82353218e-02],
        [  3.17365433e-05,   1.59439676e-04],
        [ -2.82137964e-04,  -2.38827075e-03],
        [  1.21844515e-04,   8.06557376e-03],
        [  1.36942251e-03,  -1.11000059e-05],
        [ -5.48744945e-03,  -1.00637749e-04],
        [  1.21304322e-03,  -2.26944837e-04],
        [ -2.31869648e-11,  -1.78206413e-08],
        [  1.90909436e-09,   3.91012915e-07],
        [  2.40234739e-08,  -2.04519518e-06],
        [ -2.01968782e-07,  -3.18965224e-06],
        [ -1.98306453e-07,  -7.04881662e-10],
        [  1.67199645e-06,  -6.66193280e-09],
        [ -8.05207388e-07,   2.54126171e-07],
        [ -4.69814641e-08,   4.07231531e-08],
        [ -2.46595579e-07,   2.92825242e-07],
        [ -2.22027845e-06,   1.53332454e-07]]
 
    A = TPolyRegression(3)
    A.R = [[  6.53931110e+03],
        [ -1.85958593e+01],
        [  2.73731259e-02],
        [ -1.64016838e-05]]

    global pictures
    files = pictures.keys()
    files.remove("3900-2500.jpg")
    for f in files:
        pic = SampleImage(f, pictures[f])
        pmin = pic.Img[3]
        pmax = pic.Img[5]

        (dminx, dminy) = D.GetValue((pmin[0], pmin[1], pic.A))
        (dmaxx, dmaxy) = D.GetValue((pmax[0], pmax[1], pic.A))
        amin = A.GetValue([dminy])
        amax = A.GetValue([dmaxy])
        
        print pic.A, (dminx, dminy), (dmaxx, dmaxy), amin, amax
        
def CountB():
    global spictures
    pic = spictures["3500-2000.jpg"]
    (x0, y0) = pic["img"][0]
    (x1, y1) = pic["img"][1]
    B2000 = atan(float(x0 - x1) / (y0 - y1))
    print B2000, B2000 * 180 / pi

    pic = spictures["3500-3000.jpg"]
    (x0, y0) = pic["img"][0]
    (x1, y1) = pic["img"][1]
    B3000 = atan(float(x0 - x1) / (y0 - y1))
    print B3000, B3000 * 180 / pi
    
    s = (B2000 + B3000) / 2
    
    print s, s * 180 / pi

def TestY():
    l = TLearning()
    print l.D.GetValue((0,0,3500))
    
    l.D.R[0][1] = l.D.R[0][1] + 10

    print l.D.GetValue((0,0,3500))
    

def GetTurnMatrix(pic, Y0):
    l = TLearning()
    l.D.R[0][1] = l.D.R[0][1] - Y0
    p0 = []
    r0 = []
    for i in range(len(pic["img"])):
        p0.append(l.D.GetValue((pic["img"][i][0], pic["img"][i][1], pic["A"])))
        r0.append((pic["real"][i][0], pic["real"][i][1] - Y0))
    
    pr = TPolyRegression(1)
    pr.Learn(p0, r0)
    
    print pr.R[0]
    
def TestTM():
    global spictures
    pic = spictures["3500-2000.jpg"]

    GetTurnMatrix(pic, 0)
    GetTurnMatrix(pic, 1)
    GetTurnMatrix(pic, -1)
    GetTurnMatrix(pic, -62)

def LearningBTest():
    global spictures
    pic1 = spictures["3500-2000.jpg"]
    pic2 = spictures["3500-3000.jpg"]
    l = TLearning()
    
    #X0 = 8.9234456973
    #Y0 = -15.0297784555

    #l.D.R[0][1] = l.D.R[0][1] - Y0

    p0 = []
    r0 = []
    for i in range(len(pic1["img"])):
        p0.append(l.D.GetValue((pic1["img"][i][0], pic1["img"][i][1], pic1["A"])))
        r0.append((pic1["real"][i][0], pic1["real"][i][1]))
    
    pr = TPolyRegression(1)
    pr.Learn(p0, r0)
    
    print pr.R
    print -asin(pr.R[1][0]) * 180 / pi, -acos(pr.R[1][1]) * 180 / pi
    print -acos(pr.R[2][0]) * 180 / pi, asin(pr.R[2][1]) * 180 / pi
    
    for i in range(len(p0)):
        print pr.GetValue(p0[i]), r0[i]

    print

    p0 = []
    r0 = []
    for i in range(len(pic2["img"])):
        p0.append(l.D.GetValue((pic2["img"][i][0], pic2["img"][i][1], pic2["A"])))
        r0.append((pic2["real"][i][0], pic2["real"][i][1]))
    
    pr = TPolyRegression(1)
    pr.Learn(p0, r0)
    
    print pr.R
    print -asin(pr.R[1][0]) * 180 / pi, acos(pr.R[1][1]) * 180 / pi
    print acos(pr.R[2][0]) * 180 / pi, asin(pr.R[2][1]) * 180 / pi
    
    for i in range(len(p0)):
        print pr.GetValue(p0[i]), r0[i]

def LearningBTest2():
    global spictures
    pic1 = spictures["3500-2000.jpg"]
    l = TLearning()
    
    B = pi * 150.0 * (pic1["B"] - 2500) / 2500.0 / 180.0
    
    p0 = []
    r0 = []
    for i in range(len(pic1["img"])):
        (x, y) = l.D.GetValue((pic1["img"][i][0], pic1["img"][i][1], pic1["A"]))
        p0.append((x * cos(B) - y * sin(B), x * sin(B) + y * cos(B)))
        r0.append((pic1["real"][i][0], pic1["real"][i][1]))
        print p0[i], r0[i]
    
    pr = TPolyRegression(1)
    pr.Learn(p0, r0)
    
    print pr.R
    #print -asin(pr.R[1][0]) * 180 / pi, -acos(pr.R[1][1]) * 180 / pi
    #print -acos(pr.R[2][0]) * 180 / pi, asin(pr.R[2][1]) * 180 / pi
    
    for i in range(len(p0)):
        print pr.GetValue(p0[i]), r0[i]

    print
    
    pic2 = spictures["3500-3000.jpg"]
    l = TLearning()
    
    B = pi * 150.0 * (pic2["B"] - 2500) / 2500.0 / 180.0
    
    p0 = []
    r0 = []
    for i in range(len(pic2["img"])):
        (x, y) = l.D.GetValue((pic2["img"][i][0], pic2["img"][i][1], pic1["A"]))
        p0.append((x * cos(B) - y * sin(B), x * sin(B) + y * cos(B)))
        r0.append((pic2["real"][i][0], pic2["real"][i][1]))
        print p0[i], r0[i]
    
    pr = TPolyRegression(1)
    pr.Learn(p0, r0)
    
    print pr.R
    #print -asin(pr.R[1][0]) * 180 / pi, -acos(pr.R[1][1]) * 180 / pi
    #print -acos(pr.R[2][0]) * 180 / pi, asin(pr.R[2][1]) * 180 / pi
    
    for i in range(len(p0)):
        print pr.GetValue(p0[i]), r0[i]
    
def LearningBTest3():
    
    Y0 = -15
    
    global spictures
    pic1 = spictures["3500-2000.jpg"]
    l = TLearning()

    l.D.R[0][1] = l.D.R[0][1] - Y0
    
    B = pi * 150.0 * (pic1["B"] - 2500) / 2500.0 / 180.0 - 0.00374543533591
    
    D1 = 0
    for i in range(len(pic1["img"])):
        (x, y) = l.D.GetValue((pic1["img"][i][0], pic1["img"][i][1], pic1["A"]))
        px = x * cos(B) - y * sin(B)
        py = x * sin(B) + y * cos(B)
        rx = pic1["real"][i][0]
        ry = pic1["real"][i][1] - Y0
        d = (rx - px) * (rx - px) + (ry - py) * (ry - py)
        D1 = D1 + d
        print rx - px, ry - py, d

    print D1
    
    pic2 = spictures["3500-3000.jpg"]
    
    B = pi * 150.0 * (pic2["B"] - 2500) / 2500.0 / 180.0 - 0.00374543533591
    
    D2 = 0
    for i in range(len(pic2["img"])):
        (x, y) = l.D.GetValue((pic2["img"][i][0], pic2["img"][i][1], pic2["A"]))
        px = x * cos(B) - y * sin(B)
        py = x * sin(B) + y * cos(B)
        rx = pic2["real"][i][0]
        ry = pic2["real"][i][1] - Y0
        d = (rx - px) * (rx - px) + (ry - py) * (ry - py)
        D2 = D2 + d
        print rx - px, ry - py, d

    print D2
    print Y0, D1 + D2

def LearnWithB():
    Y0 = -15
    #Y0 = 0
    
    l = TLearning()

    l.D.R[0][1] = l.D.R[0][1] - Y0

    l.CountA()
    #print l.A.R
    
    l.DumpMatrix(l.A.R)

def GetTurnTransformation():
    global spictures
    pic = spictures["3500-3000.jpg"]
    l = TLearning()
    
    #X0 = 8.9234456973
    #Y0 = -15.0297784555
    X0 = 0
    Y0 = 0

    #l.D.R[0][1] = l.D.R[0][1] - Y0

    p0 = []
    r0 = []
    for i in range(len(pic["img"])):
        p0.append(l.D.GetValue((pic["img"][i][0], pic["img"][i][1], pic["A"])))
        r0.append((pic["real"][i][0] - X0, pic["real"][i][1] - Y0))
    
    pr = TPolyRegression(1)
    pr.Learn(p0, r0)
    
    print pr.R
    
    for i in range(len(pic["img"])):
        print pr.GetValue(p0[i]), r0[i]

    cx = pr.R[0][0]
    cy = pr.R[0][1]
    
    B = pi * 150.0 * (pic["B"] - 2500) / 2500.0 / 180.0 - 0.00374543533591
    
    a = 1 - cos(B)
    b = sin(B)
    ba = b / a
    print "sin/cos", sin(B), cos(B)
    
    x0 = (cx / 2) * ba - (cy / 2)
    y0 = (cx / 2) - (cy / 2) * ba
    
    # 8.9234456973 -15.0297784555
    print "x0/y0", x0, y0
    
    cx1 = -x0 * cos(B) + y0 * sin(B) + x0
    cy1 = -x0 * sin(B) - y0 * cos(B) + y0
    
    cx2 = y0 * sin(B)
    cy2 = y0 * (1 - cos(B)) 
    
    print "cx/cy", cx1, cy1
    
    for i in range(len(pic["img"])):
        (x,y) = p0[i]
        print x * cos(B) - y * sin(B) + cx1, x * sin(B) + y * cos(B) + cy1, r0[i]
        #print x * cos(B) - (y - y0)  * sin(B), x * sin(B) + (y - y0) * cos(B) + y0, r0[i]
        
def TestAB():
    l = TLearning()
    print l.GetAB(3500, 2600, 160, 120)

def CountGripper():
    global gripper
    
    l = TLearning()
    x = []
    y = []
    for p in gripper:
        (A, B, rx, ry) = l.GetAB(p["view"], 2500, 160, 120)
        for m in p["grab"]:
            x.append([ry, m["GR"]])
            y.append([m["A"], m["G"]])
            print ry, m["GR"], m["A"], m["G"]
    
    pr = TPolyRegression(2)
    pr.Learn(x, y)
    
    print pr.R

def LoadDump(fileName):
    f = open(fileName, 'rb')
    h = bytearray(f.read(12))
    width = h[0] + 256 * (h[1] + 256 * (h[2] + 256 * h[3]))
    height = h[4] + 256 * (h[5] + 256 * (h[6] + 256 * h[7]))
    depth = h[8] + 256 * (h[9] + 256 * (h[10] + 256 * h[11]))
    data = f.read()
    f.close()
    return (width, height, depth, data)

def DrawNet(img, d, color):
    for x in range(d, img.width, d):
        for y in range(img.height):
            img.putpixel((x, y), color)

    for y in range(d, img.height, d):
        for x in range(img.width):
            img.putpixel((x, y), color)

def TestDump():
    (width, height, depth, data) = LoadDump("../dumps/1502667194.dump")
    print (width, height, depth), width * height * depth, len(data)
    area = 30
    pr = TPolyRegression(2)
    a = []
    for y in range(area):
        for x in range(area):
            a.append((x, y))
    mx = pr.GenerateMX(a)
    #px = pr.PrepareX(a)
    
    img0 = Image.frombytes('RGB', (width, height), data)

    img = Image.new('RGB', (int(width / area) * area, int(height / area) * area))
    
    for y0 in range(0, img.height, area):
        for x0 in range(0, img.width, area):
            v = []
            for y in range(area):
                for x in range(area):
                    v.append(img0.getpixel((x0 + x, y0 + y)))
            pr.NewY(mx, v)
            print "%u-%u %3u,%3u,%3u" % (x0 / area, y0 / area, pr.R[0][0], pr.R[0][1], pr.R[0][2])
            for y in range(area):
                for x in range(area):
                    pixel = pr.GetValue((x,y))
                    img.putpixel((x0 + x, y0 + y), (int(pixel[0]), int(pixel[1]), int(pixel[2])))

    img.save('d1.png', 'PNG')
    
    DrawNet(img0, area, (255,255,255))
    img0.save('d0.png', 'PNG')

def ConvertDumps():
    files = ['1502667084', '1502667129', '1502667148', '1502667166', '1502667194']
    for file in files:
        (width, height, depth, data) = LoadDump("../dumps/%s.dump" % file)
        img = Image.frombytes('RGB', (width, height), data)
        img.save("%s.png" % file, 'PNG')

"""
Green

0-2500: 71753
2500-5000: 4224
5000-7500: 585
7500-10000: 161
10000-12500: 39
12500-15000: 3
15000-17500: 4
17500-20000: 3
20000-22500: 8
22500-25000: 2
25000-27500: 2
27500-30000: 4
30000-32500: 1
32500-35000: 2
35000-37500: 0
37500-40000: 2
40000-42500: 0
42500-45000: 1
45000-47500: 2
47500-*****: 4

Blue

0-2500: 71790
2500-5000: 402
5000-7500: 248
7500-10000: 503
10000-12500: 797
12500-15000: 2264
15000-17500: 791
17500-20000: 4
20000-22500: 1
22500-25000: 0
25000-27500: 0
27500-30000: 0
30000-32500: 0
32500-35000: 0
35000-37500: 0
37500-40000: 0
40000-42500: 0
42500-45000: 0
45000-47500: 0
47500-*****: 0


Green

0-1000: 67906
1000-2000: 3350
2000-3000: 833
3000-4000: 874
4000-5000: 3014
5000-6000: 496
6000-7000: 52
7000-8000: 69
8000-9000: 46
9000-10000: 83
10000-11000: 26
11000-12000: 12
12000-13000: 2
13000-14000: 2
14000-15000: 0
15000-16000: 3
16000-17000: 1
17000-18000: 2
18000-19000: 1
19000-*****: 28

Blue

0-1000: 67290
1000-2000: 4012
2000-3000: 675
3000-4000: 133
4000-5000: 82
5000-6000: 88
6000-7000: 93
7000-8000: 154
8000-9000: 208
9000-10000: 208
10000-11000: 305
11000-12000: 258
12000-13000: 532
13000-14000: 899
14000-15000: 1067
15000-16000: 629
16000-17000: 157
17000-18000: 7
18000-19000: 1
19000-*****: 2

"""

pictures = {
    "1502667084": [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ],
    '1502667129': [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ],
    '1502667148': [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ],
    '1502667166': [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ],
    '1502667194': [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ]
    }

class Dump:
    def __init__(self, file):
        (self.Width, self.Height, self.Depth, self.Data) = LoadDump(file)
    
    def SaveAsPicture(self, file, format, scale=1):
        img = Image.frombytes('RGB', (self.Width, self.Height), self.Data)
        if scale != 1:
            img = img.resize((int(self.Width * scale), int(self.Height * scale)), Image.ANTIALIAS)
        img.save(file, format)
    
    def GetPixel(self, x, y):
        base = ((y * self.Width) + x) * self.Depth
        return [self.Data[base], self.Data[base + 1], self.Data[base + 2]]
    
    def GetDict(self):
        return {"width": self.Width, "height": self.Height, "depth": self.Depth, "data": map(ord, self.Data)}

def DrawRect(img, x, y, w, h, c):
    for i in range(w):
        img.putpixel((x + i, y), c)
        img.putpixel((x + i, y + h - 1), c)
    for i in range(h):
        img.putpixel((x, y + i), c)
        img.putpixel((x + w - 1, y + i), c)

class DeepLearning:
    
    def __init__(self):
        self.LabelArea = 10
    
    def CountL1(self, img, lx, ly):
        v = []
        for y in range(self.ScaledLabeAarea):
            for x in range(self.ScaledLabeAarea):
                v.append(img.getpixel((lx * self.ScaledLabeAarea + x, ly * self.ScaledLabeAarea + y)))
        self.Pr1.NewY(self.Mx1, v)
        v2 = []
        for row in self.Pr1.R:
            v2.extend(row)
        return v2
    
    def Learn(self, pictures, l1, l2):
        self.AreaScale = 1
        self.ScaledLabeAarea = self.LabelArea * self.AreaScale
        self.Pr1 = TPolyRegression(l1)
        self.Pr2 = TPolyRegression(l2)
    
        a = []
        for y in range(self.ScaledLabeAarea):
            for x in range(self.ScaledLabeAarea):
                a.append((x - self.ScaledLabeAarea/2, y - self.ScaledLabeAarea/2))
        self.Mx1 = self.Pr1.GenerateMX(a)
    
        X = []
        Y = []
        starttime = datetime.datetime.now()
        for file, labels in pictures.items():
            (width, height, depth, data) = LoadDump("../dumps/%s.dump" % file)
            img = Image.frombytes('RGB', (width, height), data)
            for ly in range(len(labels)):
                for lx in range(len(labels[ly])):
                    X.append(self.CountL1(img, lx, ly))
                    Y.append([0, 1, 1][labels[ly][lx]])
    
        self.Pr2.Learn(X, Y)

        endlearningtime = datetime.datetime.now()
        return endlearningtime - starttime

    def DrawResult(self, filein, fileout):
        (width, height, depth, data) = LoadDump("../dumps/%s.dump" % filein)
        img = Image.frombytes('RGB', (width, height), data)

        levelscolor = [(0.5, (255,255,255)),
                       (0.4, (255, 0 ,0)),
                       (0.3, (0, 255, 0)),
                       (0.2, (0, 0, 255))]

        startanalysistime = datetime.datetime.now()
    
        for ly in range(height / self.ScaledLabeAarea):
            for lx in range(width / self.ScaledLabeAarea):
                objlevel = self.Pr2.GetValue(self.CountL1(img, lx, ly))
                
                for level,color in levelscolor:
                    if objlevel >= level:                
                        DrawRect(img, lx * self.ScaledLabeAarea, ly * self.ScaledLabeAarea, self.ScaledLabeAarea, self.ScaledLabeAarea, color)
                        break

        endtime = datetime.datetime.now()
        print "analyze(%d, %d):%s" % (self.Pr1.S, self.Pr2.S, str(endtime - startanalysistime))

        img.save(fileout, "PNG")

    def DrawErrors(self, filein, fileout, level, labels):
        (width, height, depth, data) = LoadDump("../dumps/%s.dump" % filein)
        img = Image.frombytes('RGB', (width, height), data)
    
        negative = (255, 255, 255)
        falsepositive = (255, 0, 0)
    
        for ly in range(height / self.ScaledLabeAarea):
            for lx in range(width / self.ScaledLabeAarea):
                if self.Pr2.GetValue(self.CountL1(img, lx, ly)) > level:
                    if labels[ly][lx] == 0:
                        DrawRect(img, lx * self.ScaledLabeAarea, ly * self.ScaledLabeAarea, self.ScaledLabeAarea, self.ScaledLabeAarea, falsepositive)
                else:
                    if labels[ly][lx] > 0:
                        DrawRect(img, lx * self.ScaledLabeAarea, ly * self.ScaledLabeAarea, self.ScaledLabeAarea, self.ScaledLabeAarea, negative)

        img.save(fileout, "PNG")

    def CountOptimalThreshold(self, learningSet):
        result = []
        starttime = datetime.datetime.now()
        for file, labels in learningSet.items():
            (width, height, depth, data) = LoadDump("../dumps/%s.dump" % file)
            img = Image.frombytes('RGB', (width, height), data)
            for ly in range(height / self.ScaledLabeAarea):
                for lx in range(width / self.ScaledLabeAarea):
                    result.append((self.Pr2.GetValue(self.CountL1(img, lx, ly)), labels[ly][lx]))
        endtime = datetime.datetime.now()
        threshold = 0.0
        maxhit = 0
        while threshold < 1.0:
            hit = 0
            for v,l in result:
                if (v > threshold and l > 0) or (v <= threshold and l == 0):
                    hit = hit + 1 
            if hit >= maxhit:
                maxhit = hit
                bestthreshold = threshold
            threshold = threshold + 0.01
        return maxhit, bestthreshold, endtime - starttime, len(result)

def LearnFromPicture2():
    global pictures
    
    cw = '1502667194'
    
    del pictures[cw]

    dl = DeepLearning()
    for l1,l2 in [(1,1), (1,2), (2,1), (2,2), (3,1), (3,2), (1,3), (2, 3)]:
        dl.Learn(pictures, l1, l2)
        dl.DrawResult(cw, "cw_%d_%d_b.png" % (dl.Pr1.S, dl.Pr2.S))

def CountOptimal():
    global pictures
    
    cw = '1502667194'
    cwLabels = pictures[cw]
    
    del pictures[cw]

    dl = DeepLearning()
    results = []
    for l1,l2 in [(1,1), (1,2), (2,1), (2,2), (3,1), (3,2), (1,3), (2, 3)]:
        ltime = dl.Learn(pictures, l1, l2)
        (maxhit, bestthreshold, rtime, setsize) = dl.CountOptimalThreshold({cw:cwLabels})
        results.append((l1, l2, setsize - maxhit, bestthreshold, ltime, rtime))
        dl.DrawErrors(cw, "cw_%d_%d_e.png" % (dl.Pr1.S, dl.Pr2.S), bestthreshold, cwLabels)
    
    for l1, l2, minerror, bestthreshold, ltime, rtime in sorted(results, key=lambda res: res[2]):
        print "%d %d %3d %3.2f %s %s" % (l1, l2, minerror, bestthreshold, str(ltime), str(rtime))

def CountOptimal2():
    global pictures

    dl = DeepLearning()
    results = []
    for l1,l2 in [(1,2), (2,2)]:
        dl.Learn(pictures, l1, l2)
        for pic,labels in pictures.items():
            (maxhit, bestthreshold, rtime, setsize) = dl.CountOptimalThreshold({pic:labels})
            print "%s: %d %d %3d %3.2f %s" % (pic, l1, l2, setsize - maxhit, bestthreshold, str(rtime))

def CountOptimal3():
    global pictures

    dl = DeepLearning()
    results = []
    for l1,l2 in [(1,1), (1,2), (2,1), (2,2), (3,1), (3,2), (1,3), (2, 3)]:
        ltime = dl.Learn(pictures, l1, l2)
        (maxhit, bestthreshold, rtime, setsize) = dl.CountOptimalThreshold(pictures)
        results.append((l1, l2, setsize - maxhit, bestthreshold, ltime, rtime))
        #dl.DrawErrors(cw, "cw_%d_%d_e.png" % (dl.Pr1.S, dl.Pr2.S), bestthreshold, cwLabels)
        print l1,l2, rtime
    
    for l1, l2, minerror, bestthreshold, ltime, rtime in sorted(results, key=lambda res: res[2]):
        print "%d %d %3d %3.2f %s %s" % (l1, l2, minerror, bestthreshold, str(ltime), str(rtime))

def DumpSmall():
    dump = Dump("../dumps/%s.dump" % "1502667194")
    dump.SaveAsPicture("a.png", "PNG", 0.1)

def MakeJSONDump():
    dumps = ['1502667084', '1502667129', '1502667148', '1502667166', '1502667194']
    pics = {}
    for dumpName in dumps:
        pics[dumpName] = Dump("../dumps/%s.dump" % dumpName).GetDict()
    print json.dumps(pics)
  
#Test2()
#Im1()
#Draw1("3500-2500.jpg")
#DrawTurn("3500-2500.jpg")
#DrawTurn2("3500-2500.jpg")
#DrawTurn2("3700-2500.jpg")
#DrawTurn2("2100-2500.jpg")
#DrawTurn3("2100-2500.jpg")
#TestLinarg()
#DrawTurn4("2100-2500.jpg")
#DrawTurn5("2100-2500.jpg")
#PolyTest()
#DrawTurn6("2100-2500.jpg")
#DrawTurn7()
#DrawTurn8("2100-2500.jpg")
#DrawTurn9()
#TestEq()
#LearnA()
#TestA2()
#CountB()
#TestY()
#TestTM()
#LearningBTest()
#LearningBTest2()
#LearningBTest3()
#LearnWithB()
#GetTurnTransformation()
#TestAB()
#CountGripper()
#TestDump()
#ConvertDumps()
#LearnFromPicture()
#LearnFromPicture2()
#CountOptimal()
#CountOptimal2()
#CountOptimal3()
#DumpSmall()
MakeJSONDump()
