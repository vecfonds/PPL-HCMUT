import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_1_valid_keywords(self):
        self.assertTrue(TestLexer.test("""Break Continue If Elseif Else Foreach True False Array In Int Float Boolean String Return Null Class Val Var Constructor Destructor New By""",
                                       "Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,Null,Class,Val,Var,Constructor,Destructor,New,By,<EOF>",
                                       101))

    def test_2_valid_comment(self):
        self.assertTrue(TestLexer.test(
            """/*This is comment*/""", "<EOF>", 102))

    def test_3_error_comment(self):
        self.assertTrue(TestLexer.test(
            """/*This is comment""", "/,*,This,is,comment,<EOF>", 103))

    def test_4_error_not_close_comment(self):
        self.assertTrue(TestLexer.test(
            """/*This is comment*/*/""", "*,/,<EOF>", 104))

    def test_5_valid_ID(self):
        self.assertTrue(TestLexer.test(
            """_Sp Pk_ $H_D ALL ss""", "_Sp,Pk_,Error Token $", 105))

    def test_6_invalid_ID(self):
        self.assertTrue(TestLexer.test("""1Sp 2Pk_ 3$H_D 4ALL 5ss""",
                        "1,Sp,2,Pk_,3,Error Token $", 106))

    def test_7_two_comment(self):
        self.assertTrue(TestLexer.test(
            """##This is## abc ##comment##""", "Error Token #", 107))

    def test_8_literal_integer_valid_DEC(self):
        self.assertTrue(TestLexer.test(
            """12345 67890 0""", "12345,67890,0,<EOF>", 108))

    def test_9_literal_integer_valid_BIN(self):
        self.assertTrue(TestLexer.test(
            """0b0 0B11111 0b100000""", "0,b0,0,B11111,0,b100000,<EOF>", 109))

    def test_10_literal_integer_valid_OCT(self):
        self.assertTrue(TestLexer.test("""00 011111 0100000""",
                        "0,0,0,11111,0,100000,<EOF>", 110))

    def test_11_literal_integer_valid_HEX(self):
        self.assertTrue(TestLexer.test(
            """0x0 0X11111 0x100000""", "0,x0,0,X11111,0,x100000,<EOF>", 111))

    def test_12_literal_integer_invalid_a_number_DEC(self):
        self.assertTrue(TestLexer.test("""0000""", "0,0,0,0,<EOF>", 112))

    def test_13_literal_integer_invalid_a_number_BIN(self):
        self.assertTrue(TestLexer.test("""0b00""", "0,b00,<EOF>", 113))

    def test_14_literal_integer_invalid_a_number_OCT(self):
        self.assertTrue(TestLexer.test("""00000""", "0,0,0,0,0,<EOF>", 114))

    def test_15_literal_integer_invalid_a_number_HEX(self):
        self.assertTrue(TestLexer.test("""0x00""", "0,x00,<EOF>", 115))

    def test_16_literal_integer_delete_underscores(self):
        self.assertTrue(TestLexer.test("""1_234_567""", "1234567,<EOF>", 116))

    def test_17_literal_float_delete_underscores(self):
        self.assertTrue(TestLexer.test(
            """1_234_567.123""", "1234567.123,<EOF>", 117))

    def test_18_literal_float_component_1_2(self):
        self.assertTrue(TestLexer.test("""1.234""", "1.234,<EOF>", 118))

    def test_19_literal_float_exponent_e(self):
        self.assertTrue(TestLexer.test(
            """1.234e123""", "1.234e123,<EOF>", 119))

    def test_20_literal_float_exponent_E(self):
        self.assertTrue(TestLexer.test(
            """1.234E123""", "1.234E123,<EOF>", 120))

    def test_21_literal_float_component_1_3(self):
        self.assertTrue(TestLexer.test("""1e123""", "1e123,<EOF>", 121))

    def test_22_literal_float_component_1_3_sign(self):
        self.assertTrue(TestLexer.test(
            """1.234E-123""", "1.234E-123,<EOF>", 122))

    def test_23_literal_boolean(self):
        self.assertTrue(TestLexer.test(
            """True False""", "True,False,<EOF>", 123))

    def test_24_valid_keyword_break(self):
        self.assertTrue(TestLexer.test("""Break""", "Break,<EOF>", 124))

    def test_25_valid_keyword_continue(self):
        self.assertTrue(TestLexer.test("""Continue""", "Continue,<EOF>", 125))

    def test_26_valid_keyword_if(self):
        self.assertTrue(TestLexer.test("""If""", "If,<EOF>", 126))

    def test_27_valid_keyword_elseif(self):
        self.assertTrue(TestLexer.test("""Elseif""", "Elseif,<EOF>", 124))

    def test_28_valid_keyword_else(self):
        self.assertTrue(TestLexer.test("""Else""", "Else,<EOF>", 128))

    def test_29_valid_keyword_foreach(self):
        self.assertTrue(TestLexer.test("""Foreach""", "Foreach,<EOF>", 129))

    def test_30_valid_keyword_True(self):
        self.assertTrue(TestLexer.test("""True""", "True,<EOF>", 130))

    def test_31_valid_keyword_False(self):
        self.assertTrue(TestLexer.test("""False""", "False,<EOF>", 131))

    def test_32_valid_keyword_Array(self):
        self.assertTrue(TestLexer.test("""Array""", "Array,<EOF>", 132))

    def test_33_valid_keyword_In(self):
        self.assertTrue(TestLexer.test("""In""", "In,<EOF>", 133))

    def test_34_valid_keyword_Int(self):
        self.assertTrue(TestLexer.test("""Int""", "Int,<EOF>", 134))

    def test_35_valid_keyword_float(self):
        self.assertTrue(TestLexer.test("""Float""", "Float,<EOF>", 135))

    def test_36_valid_keyword_boolean(self):
        self.assertTrue(TestLexer.test("""Boolean""", "Boolean,<EOF>", 136))

    def test_37_valid_keyword_String(self):
        self.assertTrue(TestLexer.test("""String""", "String,<EOF>", 137))

    def test_38_valid_keyword_return(self):
        self.assertTrue(TestLexer.test("""Return""", "Return,<EOF>", 138))

    def test_39_valid_keyword_null(self):
        self.assertTrue(TestLexer.test("""Null""", "Null,<EOF>", 139))

    def test_40_valid_keyword_Class(self):
        self.assertTrue(TestLexer.test("""Class""", "Class,<EOF>", 140))

    def test_41_valid_keyword_var(self):
        self.assertTrue(TestLexer.test("""Var""", "Var,<EOF>", 141))

    def test_42_valid_keyword_val(self):
        self.assertTrue(TestLexer.test("""val""", "val,<EOF>", 142))

    def test_43_valid_keyword_self(self):
        self.assertTrue(TestLexer.test("""Self""", "Self,<EOF>", 143))

    def test_44_valid_keyword_constructor(self):
        self.assertTrue(TestLexer.test(
            """Constructor""", "Constructor,<EOF>", 144))

    def test_45_valid_keyword_Destructor(self):
        self.assertTrue(TestLexer.test(
            """Destructor""", "Destructor,<EOF>", 145))

    def test_46_valid_keyword_New(self):
        self.assertTrue(TestLexer.test("""New""", "New,<EOF>", 146))

    def test_47_valid_operator_type_static_access(self):
        self.assertTrue(TestLexer.test("""::::""", "::,::,<EOF>", 147))

    def test_48_valid_operator_type_instant_access(self):
        self.assertTrue(TestLexer.test(""".""", ".,<EOF>", 148))

    def test_49_valid_operator_type_index_operator(self):
        self.assertTrue(TestLexer.test("""[][]""", "[,],[,],<EOF>", 149))

    def test_50_valid_operator_type_sign(self):
        self.assertTrue(TestLexer.test("""---""", "-,-,-,<EOF>", 150))

    def test_51_valid_operator_type_logical_1(self):
        self.assertTrue(TestLexer.test("""!!!""", "!,!,!,<EOF>", 151))

    def test_52_valid_operator_type_multiplying(self):
        self.assertTrue(TestLexer.test("""*/%""", "*,/,%,<EOF>", 152))

    def test_53_valid_operator_type_add(self):
        self.assertTrue(TestLexer.test("""+-""", "+,-,<EOF>", 153))

    def test_54_valid_operator_type_logical_2(self):
        self.assertTrue(TestLexer.test("""&&||""", "&&,||,<EOF>", 154))

    def test_55_valid_operator_type_relational(self):
        self.assertTrue(TestLexer.test(
            """== != < > <= >=""", "==,!=,<,>,<=,>=,<EOF>", 155))

    def test_56_valid_operator_type_string(self):
        self.assertTrue(TestLexer.test("""+. ==.""", "+,.,==,.,<EOF>", 156))

    def test_57_error_token_1(self):
        self.assertTrue(TestLexer.test(
            """abcde?fghiklmno""", "abcde,Error Token ?", 157))

    def test_58_error_token_2(self):
        self.assertTrue(TestLexer.test(
            """abcde^fghiklmno""", "abcde,Error Token ^", 158))

    def test_59_error_token_3(self):
        self.assertTrue(TestLexer.test(
            """abcde@fghiklmno""", "abcde,Error Token @", 159))

    def test_60_error_token_4(self):
        self.assertTrue(TestLexer.test(
            """abcde#fghiklmno""", "abcde,Error Token #", 160))

    def test_61_error_token_5(self):
        self.assertTrue(TestLexer.test(
            """abcde|fghiklmno""", "abcde,Error Token |", 161))

    def test_62_valid_token_1(self):
        self.assertTrue(TestLexer.test(
            """Return 1;""", "Return,1,;,<EOF>", 162))

    def test_63_valid_token_2(self):
        self.assertTrue(TestLexer.test(
            """Array[Int,10]""", "Array,[,Int,,,10,],<EOF>", 163))

    def test_64_valid_token_3(self):
        self.assertTrue(TestLexer.test(
            """Class Hello{}""", "Class,Hello,{,},<EOF>", 164))

    def test_65_valid_token_4(self):
        self.assertTrue(TestLexer.test("""Var a,b: Int;""",
                        "Var,a,,,b,:,Int,;,<EOF>", 165))

    def test_66_valid_token_5(self):
        self.assertTrue(TestLexer.test("""Val a,b: Int;""",
                        "Val,a,,,b,:,Int,;,<EOF>", 166))

    def test_67_literal_string_valid_1(self):
        self.assertTrue(TestLexer.test(""" "abcd" """, "abcd,<EOF>", 167))

    def test_68_literal_string_invalid_2(self):
        self.assertTrue(TestLexer.test(
            """ "abc\bd" """, "Unclosed String: abc", 168))

    def test_69_literal_string_invalid_3(self):
        self.assertTrue(TestLexer.test(
            """ "abc\fd" """, "Unclosed String: abc", 169))

    def test_70_literal_string_invalid_4(self):
        self.assertTrue(TestLexer.test(
            """ "abc\rd" """, "Unclosed String: abc", 170))

    def test_71_literal_string_invalid_5(self):
        self.assertTrue(TestLexer.test(
            """ "abc\nd" """, "Unclosed String: abc", 171))

    def test_72_literal_string_invalid_6(self):
        self.assertTrue(TestLexer.test(
            """ "abc\'d" """, "Unclosed String: abc", 172))

    def test_73_literal_string_invalid_7(self):
        self.assertTrue(TestLexer.test(""" "abc\\d" """,
                        "Illegal Escape In String: abc\d", 173))

    def test_74_literal_string_invalid_8(self):
        self.assertTrue(TestLexer.test(
            """ "abc\td" """, "Unclosed String: abc", 174))

    def test_75_literal_string_invalid_9(self):
        self.assertTrue(TestLexer.test(""" "abc\\od" """,
                        "Illegal Escape In String: abc\o", 175))

    def test_76_literal_string_invalid_10(self):
        self.assertTrue(TestLexer.test(""" "abc\\id" """,
                        "Illegal Escape In String: abc\i", 176))

    def test_77_literal_string_invalid_11(self):
        self.assertTrue(TestLexer.test(""" "abc\\pd" """,
                        "Illegal Escape In String: abc\p", 177))

    def test_78_literal_string_invalid_12(self):
        self.assertTrue(TestLexer.test(""" "abc\\ld" """,
                        "Illegal Escape In String: abc\l", 178))

    def test_79_literal_string_invalid_13(self):
        self.assertTrue(TestLexer.test(""" "abc\\hd" """,
                        "Illegal Escape In String: abc\h", 179))

    def test_80_literal_string_invalid_14(self):
        self.assertTrue(TestLexer.test(""" "abc\\yd" """,
                        "Illegal Escape In String: abc\y", 180))

    def test_81_literal_string_invalid_15(self):
        self.assertTrue(TestLexer.test(""" "abc\\gd" """,
                        "Illegal Escape In String: abc\g", 181))

    def test_82_literal_integer1(self):
        self.assertTrue(TestLexer.test(
            """10100011001100_101010101""", "10100011001100101010101,<EOF>", 182))

    def test_83_literal_integer2(self):
        self.assertTrue(TestLexer.test(
            """0x1234567678_4552323ADFG0X000""", "0,x1234567678_4552323ADFG0X000,<EOF>", 183))

    def test_84_literal_integer3(self):
        self.assertTrue(TestLexer.test(
            """0xABCDEF000b00111111111""", "0,xABCDEF000b00111111111,<EOF>", 184))

    def test_85_literal_integer4(self):
        self.assertTrue(TestLexer.test(
            """1234560b110011001100""", "1234560,b110011001100,<EOF>", 185))

    def test_86_literal_integer5(self):
        self.assertTrue(TestLexer.test("""0000000000000000000""",
                        "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,<EOF>", 186))

    def test_87_literal_integer6(self):
        self.assertTrue(TestLexer.test(
            """0b000x000X000B00001122334455""", "0,b000x000X000B00001122334455,<EOF>", 187))

    def test_88_literal_integer7(self):
        self.assertTrue(TestLexer.test(
            """0xCAFFAADFFFF0b00234""", "0,xCAFFAADFFFF0b00234,<EOF>", 188))

    def test_89_literal_integer8(self):
        self.assertTrue(TestLexer.test(
            """0B00b02453556333210xACFD""", "0,B00b02453556333210xACFD,<EOF>", 189))

    def test_90_literal_integer9(self):
        self.assertTrue(TestLexer.test(
            """2342344000x0000b0002324342""", "2342344000,x0000b0002324342,<EOF>", 190))

    def test_91_literal_integer10(self):
        self.assertTrue(TestLexer.test("""99999990x999afd""",
                        "99999990,x999afd,<EOF>", 191))

    def test_92_literal_integer11(self):
        self.assertTrue(TestLexer.test(
            """0b1000000000010000000""", "0,b1000000000010000000,<EOF>", 192))

    def test_93_literal_integer12(self):
        self.assertTrue(TestLexer.test(
            """0000b100010x123233003434""", "0,0,0,0,b100010x123233003434,<EOF>", 193))

    def test_94_literal_integer13(self):
        self.assertTrue(TestLexer.test(
            """0xADFC00b101010101010""", "0,xADFC00b101010101010,<EOF>", 194))

    def test_95_literal_integer14(self):
        self.assertTrue(TestLexer.test("""345456654640x134353534acfd00b0101010101""",
                        "345456654640,x134353534acfd00b0101010101,<EOF>", 195))

    def test_96_literal_integer15(self):
        self.assertTrue(TestLexer.test(
            """0x111111111002345535""", "0,x111111111002345535,<EOF>", 196))

    def test_97_literal_integer16(self):
        self.assertTrue(TestLexer.test(
            """0b10101010100x32423342234acccc""", "0,b10101010100x32423342234acccc,<EOF>", 197))

    def test_98_literal_integer17(self):
        self.assertTrue(TestLexer.test("""0XAAAAAAAAFFFFFFF0b10101010100x11111""",
                        "0,XAAAAAAAAFFFFFFF0b10101010100x11111,<EOF>", 198))

    def test_99_literal_integer18(self):
        self.assertTrue(TestLexer.test(
            """12345639852500xAAAAAAAAAAA""", "12345639852500,xAAAAAAAAAAA,<EOF>", 199))

    def test_99_literal_integer18(self):
        self.assertTrue(TestLexer.test(
            """12345639852500xAAAAAAAAAAA""", "12345639852500,xAAAAAAAAAAA,<EOF>", 199))
