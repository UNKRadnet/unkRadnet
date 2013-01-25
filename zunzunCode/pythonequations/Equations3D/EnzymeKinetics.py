#    pythonequations is a collection of equations expressed as Python classes
#    Copyright (C) 2008 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#    email: zunzun@zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)
#    Version info: $Id: EnzymeKinetics.py 274 2010-09-29 13:16:14Z zunzun.com $

import pythonequations, pythonequations.EquationBaseClasses, pythonequations.ExtraCodeForEquationBaseClasses
import numpy
numpy.seterr(all = 'raise') # numpy raises warnings, convert to exceptions to trap them


class InhibitionByCompetingSubstrateA3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = False
    _name ="Inhibition By Competing Substrate A"
    _HTML = "z = (ax/b) / (1 + x/b + y/c)"
    coefficientDesignatorTuple = ("a", "b", 'c')
    function_cpp_code = 'temp = coeff[0] * _id[_cwo[0]+i] / coeff[1] / (1.0 + _id[_cwo[0]+i] / coeff[1] + _id[_cwo[1]+i] / coeff[2]);'

    x_in = 'x_in'
    y_in = 'y_in'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * " + self.x_in + " / (b * " + self.x_in + " + c * " + self.y_in + " + " + self.x_in + " * y)in);\n"
        return s



class InhibitionByCompetingSubstrateB3D(InhibitionByCompetingSubstrateA3D):
    _name ="Inhibition By Competing Substrate B"
    _HTML = "z = (ay/b) / (1 + y/b + x/c)"

    x_in = 'y_in'
    y_in = 'x_in'

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])



class PingPongBiBiA3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = False
    _name ="Ping Pong Bi Bi A"
    _HTML = "z = ax / (bx + cy + xy)"
    coefficientDesignatorTuple = ("a", "b", 'c')
    function_cpp_code = 'temp = coeff[0] * _id[_cwo[0]+i] / (coeff[1] * _id[_cwo[0]+i] + coeff[2] * _id[_cwo[1]+i] + _id[_cwo[0]+i] * _id[_cwo[1]+i]);'

    x_in = 'x_in'
    y_in = 'y_in'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * " + self.x_in + " / (b * " + self.x_in + " + c * " + self.y_in + " + " + self.x_in + " * y)in);\n"
        return s



class PingPongBiBiB3D(PingPongBiBiA3D):
    _name ="Ping Pong Bi Bi B"
    _HTML = "z = ay / (by + cx + xy)"

    x_in = 'y_in'
    y_in = 'x_in'

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])



class MixedInhibitionA3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = False
    _name ="Mixed Inhibition A"
    _HTML = "z = ax / (b(1 + y/c) + x(1 + y/d))"
    coefficientDesignatorTuple = ("a", "b", 'c', 'd')
    function_cpp_code = 'temp = coeff[0] * _id[_cwo[0]+i] / ((coeff[1] * (1.0 + _id[_cwo[1]+i] / coeff[2])) + _id[_cwo[0]+i] * (1.0 + _id[_cwo[1]+i] / coeff[3]));'

    x_in = 'x_in'
    y_in = 'y_in'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * " + self.x_in + " / ((b * (1.0 + " + self.y_in + " / c) + (" + self.x_in + " * (1.0 + " + self.y_in + " / d)));\n"
        return s



class MixedInhibitionB3D(MixedInhibitionA3D):
    _name ="Mixed Inhibition B"
    _HTML = "z = ay / (b(1 + x/c) + y(1 + x/d))"

    x_in = 'y_in'
    y_in = 'x_in'

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])



class NoncompetitiveInhibitionA3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = False
    _name ="Noncompetitive Inhibition A"
    _HTML = "z = ax / ((b + x)(1 + y/c))"
    coefficientDesignatorTuple = ("a", "b", 'c')
    function_cpp_code = 'temp = coeff[0] * _id[_cwo[0]+i] / ((coeff[1] + _id[_cwo[0]+i]) * (1.0 + _id[_cwo[1]+i] / coeff[2]));'

    x_in = 'x_in'
    y_in = 'y_in'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * " + self.x_in + " / ((b + " + self.x_in + ") * (1.0 + " + self.y_in + " / c));\n"
        return s



class NoncompetitiveInhibitionB3D(NoncompetitiveInhibitionA3D):
    _name ="Noncompetitive Inhibition B"
    _HTML = "z = ay / ((b + y)(1 + x/c))"

    x_in = 'y_in'
    y_in = 'x_in'

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])



class UncompetitiveInhibitionA3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = False
    _name ="Uncompetitive Inhibition A"
    _HTML = "z = ax / (b + x(1 + y/c))"
    coefficientDesignatorTuple = ("a", "b", 'c')
    function_cpp_code = 'temp = coeff[0] * _id[_cwo[0]+i] / (coeff[1] + _id[_cwo[0]+i] * (1.0 + _id[_cwo[1]+i] / coeff[2]));'

    x_in = 'x_in'
    y_in = 'y_in'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * " + self.x_in + " / (b + " + self.x_in + " * (1.0 + " + self.y_in + " / c));\n"
        return s



class UncompetitiveInhibitionB3D(UncompetitiveInhibitionA3D):
    _name ="Uncompetitive Inhibition B"
    _HTML = "z = ay / (b + y(1 + x/c))"

    x_in = 'y_in'
    y_in = 'x_in'

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])



class CompetitiveInhibitionA3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = False
    _name ="Competitive Inhibition A"
    _HTML = "z = ax / (b(1 + y/c) + x)"
    coefficientDesignatorTuple = ("a", "b", 'c')
    function_cpp_code = 'temp = coeff[0] * _id[_cwo[0]+i] / (coeff[1] * (1.0 + _id[_cwo[1]+i] / coeff[2]) + _id[_cwo[0]+i]);'

    x_in = 'x_in'
    y_in = 'y_in'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * " + self.x_in + " / (b * (1.0 + " + self.y_in + " / c) + " + self.x_in + ");\n"
        return s



class CompetitiveInhibitionB3D(CompetitiveInhibitionA3D):
    _name ="Competitive Inhibition B"
    _HTML = "z = ay / (b(1 + x/c) + y)"

    x_in = 'y_in'
    y_in = 'x_in'

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])



class MichaelisMentenProductInhibition3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name ="Michaelis Menten Product Inhibition"
    _HTML = "z = (ax/b - cy/d) / (1 + x/b + y/d)"
    coefficientDesignatorTuple = ("a", "b", 'c', 'd')
    function_cpp_code = 'temp = (coeff[0] * _id[_cwo[0]+i] / coeff[1] - coeff[2] * _id[_cwo[1]+i] / coeff[3]) / (1.0 + _id[_cwo[0]+i] / coeff[1] + _id[_cwo[1]+i] / coeff[3]);'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = (a * x_in / b - c * y_in / d) / (1.0 + x_in / b + y_in / d);\n"
        return s