import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # def test_short_vardecl(self):
    #     input = """x: integer;"""
    #     expect = str(Program([VarDecl("x", IntegerType())]))
    #     self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""

        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
            a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
                printInteger(4);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_6(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_7(self):
        input = """
            x: integer = 65;
            fact: function integer(n: integer){
            }
            """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_8(self):
        input = """
            x: integer = 65;
            fact: function integer(n: integer){
                {
                    x: integer = 65;
                    x: integer = 65;
                    x: integer = 65;
                    if(n==1){return 2;}
                    if(n==0){return 1;}
                }
            }
            """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([BlockStmt([VarDecl(x, IntegerType, IntegerLit(65)), VarDecl(x, IntegerType, IntegerLit(65)), VarDecl(x, IntegerType, IntegerLit(65)), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(2))]), ), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(1))]), )])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_9(self):
        input = """
            x: integer = 65;
            fact: function integer(n: integer){
                {
                    x: integer = 65;
                    x: integer = 65;
                    x: integer = 65;
                    if(n==1)return 2;
                    if(n==0)return 1;

                    if (n==0) {return 1;}
                    else {return n*fact(n-1);}
                }
            }
            """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([BlockStmt([VarDecl(x, IntegerType, IntegerLit(65)), VarDecl(x, IntegerType, IntegerLit(65)), VarDecl(x, IntegerType, IntegerLit(65)), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(2)), ), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))])))]))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_10(self):
        input = """
                x: integer = 65;
                fact: function integer (n: integer) {
                    if (n == 0) return 1;
                    else return n * fact(n - 1);
                }
                inc: function void(out n: integer, delta: integer) {
                    n = n + delta;
                }
                main: function void() {
                    delta: integer = fact(3);
                    inc(x, delta);
                    printInteger(x);
                }
            """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_11(self):
        input = """a: array [3] of integer;"""
        expect = """Program([
	VarDecl(a, ArrayType([3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_12(self):
        input = """
            fact: function integer(n: integer){
                    a = "aas";
            }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(a), StringLit(aas))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_13(self):
        input = """
            test: function boolean () {
                a[1]= 1;
                    for(a = 1+1, i < 10*2, i + 2) {

                    }
                }
            main: function void () {

            }"""
        expect = """Program([
	FuncDecl(test, BooleanType, [], None, BlockStmt([AssignStmt(ArrayCell(Id(a), [IntegerLit(1)]), IntegerLit(1)), ForStmt(AssignStmt(Id(a), BinExpr(+, IntegerLit(1), IntegerLit(1))), BinExpr(<, Id(i), BinExpr(*, IntegerLit(10), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_133(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_14(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_15(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_16(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_17(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_18(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_19(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_20(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_21(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_22(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_23(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_24(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_25(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_26(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_27(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_28(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_29(self):
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
         printInteger(4);
    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
