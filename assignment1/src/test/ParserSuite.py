import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_2(self):
        """Simple program: int main() {} """
        input = """
        x: integer = 65;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_3(self):
        """Simple program: int main() {} """
        input = """
        x: integer = 65;
        fact: function integer(n: integer){
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_4(self):
        """Simple program: int main() {} """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_5(self):
        """Simple program: int main() {} """
        input = """
        x: integer = 65;
        fact: function integer(n: integer){
            {
                x: integer = 65;
                x: integer = 65;
                x: integer = 65;
                if(n==1)return 2;
                if(n==0)return 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_6(self):
        """Simple program: int main() {} """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_7(self):
        """Simple program: int main() {} """
        input = """x: integer = 65;
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
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_8(self):
        """Simple program: int main() {} """
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_9(self):
        """Simple program: int main() {} """
        inp = """a, b, c: integer = 4, 5, 6, (3 + 5), 8, 9 , 19;"""
        expect = "Error on line 1 col 26: ,"
        self.assertTrue(TestParser.test(inp, expect, 209))

    def test10(self):
        input = """
        fact: function integer (n: integer, a:float, a_b: boolean, a_2b: string, bb: array [3,4,6,7] of integer) {
                            t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }
        main: function void() {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test11(self):
        input = """
        fact: function integer (n: integer, a:float, a_b: boolean, a_2b: string, bb: array [3,4,6,7] of integer) {
                            t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }
            tend: function integer (n: integer, a:float, a_b: boolean, a_2b: string, bb: array [3,4,6,7] of integer) {
            }
        main: function void() {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test12(self):
        input = """
        fact: function integer (n: integer, a:float, a_b: boolean, a_2b: string, bb: array [3,4,6,7] of integer) {
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";            }
            tend: function integer (n: integer, a:float, a_b: boolean, a_2b: string, bb: array [3,4,6,7] of integer) {
            }
        main: function void() {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test13(self):
        input = """
        fact: function integer (n: integer, a:float, a_b: boolean, a_2b: string, bb: array [3,4,6,7] of integer) {
                a = false ;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test14(self):
        input = """

        fact: function integer (n: integer, a:float, a_b: boolean, a_2b: string, bb: array [3,4,6,7] of integer) {
                a = true ;
                b = 1;
                d = 1.1;
                e = 1e-10;
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }
            tend: function integer (n: integer, a:float, a_b: boolean, a_2b: string, bb: array [3,4,6,7] of integer) {
            }
        main: function void() {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test15(self):
        input = """
        fact: function integer (out n: integer, a:float, a_b: boolean, a_2b: string, bb: array [3,4,6,7] of integer) {
            }
        main: function void() {
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test16(self):
        input = """
        cat: function void () inherit animals {
            }
        main: function void () {
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test17(self):
        input = """
         cat: function boolean () inherit animals {
                             t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }

            teacher: function float () inherit person {
            }
        main: function void () {
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test18(self):
        input = """
        cat: function boolean () inherit animals {
                            t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }

            teacher: function float () inherit person {
            }
        main: function void () {
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test19(self):
        input = """
        cat: function boolean (out a: integer, inherit voice: string) inherit animals {
                           t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }
        main: function void () {
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test20(self):
        input = """
        cat: function boolean (out a: integer, inherit voice: string) inherit animals {
            }
        main: function void () {
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test21(self):
        input = """

        test: function boolean () {
                a: integer;
                                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test22(self):
        input = """
        test: function boolean () {
                b: float;
                                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test23(self):
        input = """
        test: function boolean () {
                b: string;
                                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test24(self):
        input = """
        test: function boolean () {
                b: boolean;
                                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test25(self):
        input = """
        test: function boolean () {
                b: auto;
                                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test26(self):
        input = """
        test: function boolean () {
                            t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
                b: array [2] of integer;
            }
        main: function void () {
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test27(self):
        input = """
        test: function boolean () {
                b: array [1+1] of float;
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";               
            }
        main: function void () {
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test28(self):
        input = """

        test: function boolean () {
                b: array [1+1,2*2] of float;
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }
        main: function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test29(self):
        input = """
        test: function boolean () {
                b: array [1+1,2*2, 3%3] of float;
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test30(self):
        input = """
        test: function boolean () {
                a: integer =2_1123;
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test31(self):
        input = """
        test: function boolean () {
                b: float = 1.2e-10;
                t,v : string = "pk","pknguyen";
                b: string = "abc\\"abc\\"";
                
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test32(self):
        input = """
        test: function boolean () {
            b: string = "abc\\"abc\\"";

            }

        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test33(self):
        input = """
        test: function boolean () {
                b: boolean =true;
                t,v : string = "pk","pknguyen";
                
            }

        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test34(self):
        input = """
        test: function boolean () {
                b: auto= 1+5*2-4%2;
                t,v : string = "pk","pknguyen";
                
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test35(self):
        input = """
        test: function boolean () {
                r,s : integer = 1,2;
                t,v : string = "pk","pknguyen";
                
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test36(self):
        input = """
        test: function boolean () {
                r,s : integer = 1+0-1*7%2,2;
                t,v : string = "pk","pknguyen";
                
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test37(self):
        input = """
        test: function boolean () {
                r,s : float = 1_123.1,2e-10;
                t,v : string = "pk","pknguyen";
                
            }

        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test38(self):
        input = """
        test: function boolean () {
                r,s : array [3] of boolean = {true,true,true},{true,true,true};
                t,v : string = "pk","pknguyen";
            }
        main: function void () {
            z = 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test39(self):
        input = """
        test: function boolean () {
                r,s : boolean = true,false;
                t,v : auto = false,1+3+4+5;
                
            }
        main: function void () {
            z = 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test40(self):
        input = """
        test: function boolean () {
                r,s : auto = false,1+3+4+5;
            }
        main: function void () {
            z = 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test41(self):
        input = """
        test: function boolean () {
                r,s : array [3] of string = {"Kangxi", "Yongzheng", "Qianlong"},{"Kangxi", "Yongzheng", "Qianlong"};
            }
        main: function void () {
            z = 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test42(self):
        input = """
        test: function boolean () {
                r,s : array [3] of integer = {1,2,3},{1,2,3};
            }

        main: function void () {
            z = 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test43(self):
        input = """
        test: function boolean () {
                r,s : array [3] of integer = {1,2,3},{1,2,3};
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test44(self):
        input = """
        test: function boolean () {
                r,s : array [3] of integer = {1,2,3},{1,2,3};
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test45(self):
        input = """
        test: function boolean () {
                r,s : array [3] of integer = {1,2,3},{1,2,3};
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test46(self):
        input = """
        test: function boolean () {
                a[3] = 1 + 2;
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test47(self):
        input = """
        test: function boolean () {
            a[2+5] = 2;

            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test48(self):
        input = """
        test: function boolean () {
            a[3] = a[2];

            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test49(self):
        input = """
        test: function boolean () {
            a[3,2] = a[2,1,1];
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test50(self):
        input = """
         test: function boolean () {
            a[3+2,2-1] = a[2+2*5,1,1];
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test51(self):
        input = """
        test: function boolean () {
            A[a[2]] = a[1];
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test52(self):
        input = """
        test: function boolean () {
            a :integer = 1000;
            b :boolean = !false;
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test53(self):
        input = """
         test: function boolean () {
            a :integer = ---3;
            b :boolean = !false;

            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test54(self):
        input = """
        test: function boolean () {
            a :integer = -1000;

            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test55(self):
        input = """
        test: function boolean () {
            a :integer = 3;
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test56(self):
        input = """
        test: function boolean () {
            a :integer = ---3;
            b :boolean = !true;
            u :integer = 3;
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test57(self):
        input = """
        test: function boolean () {
            a :integer = ---3;
            b :boolean = !true;
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test58(self):
        input = """
        test: function boolean () {
            a :integer = ---3;
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test59(self):
        input = """
        test: function boolean () {
            a :integer = ---3;
            b :boolean = !true;
            u :integer = 3;
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test60(self):
        input = """
        test: function boolean () {
            a :integer = ---3;
            b :boolean = !true;
            u :integer = 3;
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test61(self):
        input = """
        test: function boolean () {
                if (1 > 2) a = a + 1 + 4;
            }

        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test62(self):
        input = """
        test: function boolean () {
                if (1 > 2) foo(1,2);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test63(self):
        input = """
        test: function boolean () {
                if (1 > 2) return 2;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test64(self):
        input = """
        test: function boolean () {
                if (1 > 2) return 1;
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test65(self):
        input = """
        test: function boolean () {
                if (1 > 2) return 1;
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test66(self):
        input = """
        test: function boolean () {
                if (1 > 2)
                    if (!true) return 2;
                else
                    if(!false) return a[2,3];

            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test67(self):
        input = """
        test: function boolean () {
                if(1+1)
                    if(true)
                        return 0;
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test68(self):
        input = """
        test: function boolean () {
                if(true) return 1;

            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test68(self):
        input = """
        test: function boolean () {
                if(true) return 2;

            }

        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test69(self):
        input = """
        test: function boolean () {
                if(true)
                    return 2 % 2;

            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test70(self):
        input = """
        test: function boolean () {
                if(true)
                    if(1)
                        return 2;

            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test71(self):
        input = """
        test: function boolean () {

            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test72(self):
        input = """
        test: function boolean () {
                for(i = 1+1, i < 10*2, i + 2) {

                }
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test73(self):
        input = """
        test: function boolean () {
                for(i = 1*1, i < 102, i + 2) {

                }
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test74(self):
        input = """
        test: function boolean () {
                for(i = 1*1, i < 102, i + 2) {

                }
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test75(self):
        input = """
        test: function boolean () {
                for(i = 1*1, i < 102, i + 2) {
                    if(true) break;
                }
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test76(self):
        input = """
        test: function boolean () {
                for(i = 1*1, i < 102, i + 2) {
                    if(i % 2 == 0) i = i + 1;
                }
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test77(self):
        input = """
        test: function boolean () {
                for(i = 1*1, i < 10/2, i + 2) {
                    if(i % 2 == 0) i = i + 1;
                }
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test78(self):
        input = """
        test: function boolean () {
                for(i = 1*1, i < 10/2, i + 2) {
                    if(i % 2 == 0)
                        if(i< 9)
                            break;
                }
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test79(self):
        input = """
        test: function boolean () {
                for(i = 1*1, i < 10, i + 5) {
                    while (i % 2 == 0)
                        if(true)
                            return 1;
                }
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test80(self):
        input = """
        test: function boolean () {
                for(i = 1*1, i < 10, i + 2) {
                    while (i % 2 == 0)
                        while(i - 1 > 0)
                            return i;
                }
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test81(self):
        input = """
        test: function boolean () {
                do {
                    a = a * a;
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test82(self):
        input = """
        test: function boolean () {
                do {
                    do {
                        a = a + 2;
                    }
                    while(a < 10);
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test83(self):
        input = """
        test: function boolean () {
                do {
                    a = a + 1;
                    do {

                        for(i = 1, i < 10, i + 1) {
                            while(true) break;
                        }
                    }
                    while(a < 10);
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test84(self):
        input = """
        test: function boolean () {
                do {
                    a = a + 1;
                    do {

                        for(i = 1, i < 10, i + 1) {
                            if(i >2) break;
                            while(i < 5) break;
                        }
                    }
                    while(a < 10);
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test85(self):
        input = """
        test: function boolean () {
                do {
                    foo(2 + x, 4.0 /y);
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test86(self):
        input = """
        test: function boolean () {
                do {
                    foo();
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test87(self):
        input = """
        test: function boolean () {
                do {
                    a = a + 1;
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test88(self):
        input = """
        test: function boolean () {
                do {
                    foo(foo(a[2,3]), foo(1));
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test89(self):
        input = """
        test: function boolean () {
                do {
                    a, b: array [5] of integer;
                    s = r * r * myPI;
                    a[0] = s;
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test89(self):
        input = """
        test: function boolean () {
                do {
                    a = 2;
                    {
                        r, s: integer;
                        r = 2.0;
                        a[0] = s;
                    }
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test90(self):
        input = """
        test: function boolean () {
                do {
                    a = 2;
                    {
                        r = 2.0;
                        {
                            a, b: array [5] of integer;
                            s = r * r * myPI;
                        }
                    }
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test91(self):
        input = """
        test: function boolean () {
                do {
                    a = 2;
                    {
                        r, s: integer;
                        r = 2.0;
                        {
                            a, b: array [5] of integer;
                        }
                    }
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test92(self):
        input = """
        test: function boolean () {
                do {
                    a = 2;
                    {
                        while(a < 10)
                        {
                            
                        }

                    }

                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test93(self):
        input = """
        test: function boolean () {
                do {
                    a = 2;
                    {
                        for(i = 1, i < 10, i*2){
                        }

                    }

                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test94(self):
        input = """
        test: function boolean () {
                do {
                    a = 2;
                    {}
                    {}
                    i = 0;
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test95(self):
        input = """
        test: function boolean () {
                do {
                    z= 1000;

                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test96(self):
        input = """
         test: function boolean () {
                do {
                    z = 3;
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test97(self):
        input = """
        test: function boolean () {
                do {
                    a = 2;
                    {{{}}}
                    {{{{{}}}}}

                }
                while (a < 20);
            }
        a, b, c, d: integer = 3, 4, 6;

        main: function void () {

        }"""
        expect = "Error on line 11 col 37: ;"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test98(self):
        input = """
        test: function boolean () {
                do {
                    a = 2;
                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test99(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
        }
        main: function void() {
            inc(x, delta);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test100(self):
        input = """
        test: function boolean () {
                do {
                    a = 5;
                    {
                        readInteger();
                        readFloat();
                        readBoolean();
                        printBoolean(!true);
                        readString();
                        printString("string");
                        preventDefault();

                    }

                }
                while (a < 20);
            }
        main: function void () {

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
