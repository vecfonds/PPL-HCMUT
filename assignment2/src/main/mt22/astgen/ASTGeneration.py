from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        # declList = []
        # for x in ctx.decllist():
        #     decl = self.visit(x)
        #     if isinstance(decl, list):
        #         declList.extend(decl if decl else [])
        #     else:
        #         declList.append(decl)
        # return Program(declList)

        declList = self.visit(ctx.decllist())

        # return Program(declList)
        return "Program([\n\t{}\n])".format("\n\t".join([str(decl) for decl in declList]))

        # return "Program([\n\t{}\n])".format("\n\t".join([str(decl) for decl in declList]))

    # Visit a parse tree produced by MT22Parser#decllist.

    def visitDecllist(self, ctx: MT22Parser.DecllistContext):
        if ctx.getChildCount() == 2:
            decl = [self.visit(ctx.decl())]
            decllist = self.visit(ctx.decllist())
            return decl + decllist
        else:
            return [self.visit(ctx.decl())]

    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#var_decl.
    def visitVar_decl(self, ctx: MT22Parser.Var_declContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#vardecl_normal.
    def visitVardecl_normal(self, ctx: MT22Parser.Vardecl_normalContext):
        idlist = self.visit(ctx.idlist())
        var_type = self.visit(ctx.var_type())
        # return VarDecl(",".join([str(id) for id in idlist]), var_type)
        res = []
        for id in idlist:
            res += ["VarDecl({}, {})".format(str(id), str(var_type))]

        return "{}".format("\n\t".join([str(a) for a in res]))
        # return "VarDecl({}, {})".format(",".join([str(id) for id in idlist]), str(var_type))

    # Visit a parse tree produced by MT22Parser#vardecl_symmetric.

    def visitVardecl_symmetric(self, ctx: MT22Parser.Vardecl_symmetricContext):
        if ctx.getChildCount() == 5:  # 2
            id = ctx.ID().getText()
            vardecl_symmetric = self.visit(ctx.vardecl_symmetric())
            exp = self.visit(ctx.exp())
            return [str(id), vardecl_symmetric, str(exp)]
        elif ctx.var_type():  # 3
            return str(self.visit(ctx.var_type()))
        else:  # 1
            id = ctx.ID().getText()
            vardecl_symmetric = self.visit(ctx.vardecl_symmetric())
            exp = self.visit(ctx.exp())

            if isinstance(vardecl_symmetric, list):
                vardecl_symmetric = [str(id)] + vardecl_symmetric + [str(exp)]
            else:
                return "VarDecl({}, {}{})".format(id, str(vardecl_symmetric), ", " + str(exp))

            flat_list = []
            # Iterate through the outer list
            for element in vardecl_symmetric:
                if type(element) is list:
                    # If the element is of type list, iterate through the sublist
                    for item in element:
                        flat_list.append(item)
                else:
                    flat_list.append(element)

            # flat_list = [str(id)] + flat_list + [str(exp)]

            mid = int(len(flat_list)/2)
            res = []
            for x in range(mid):
                res += ["VarDecl({}, {}{})".format(str(flat_list[x]),
                                                   flat_list[mid], ", " + str(flat_list[mid+x+1]))]

            return "{}".format("\n\t".join([str(a) for a in res]))

    # Visit a parse tree produced by MT22Parser#idlist.

    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 3:  # 2
            id = [ctx.ID().getText()]
            idlist = self.visit(ctx.idlist())
            return id + idlist
        else:
            return [ctx.ID().getText()]

    # Visit a parse tree produced by MT22Parser#list_exp.

    def visitList_exp(self, ctx: MT22Parser.List_expContext):
        if ctx.getChildCount() == 3:
            exp = [self.visit(ctx.exp())]
            list_exp = self.visit(ctx.list_exp())
            return exp + list_exp
        else:
            return [self.visit(ctx.exp())]

    # Visit a parse tree produced by MT22Parser#func_decl.
    def visitFunc_decl(self, ctx: MT22Parser.Func_declContext):
        id = ctx.ID(0).getText()
        func_type = self.visit(ctx.func_type())
        param_lists = self.visit(
            ctx.param_lists()) if ctx.param_lists() else []

        statement_block = self.visit(ctx.statement_block())

        return "FuncDecl({}, {}, [{}], {}, {})".format(id, str(func_type), ", ".join([str(param) for param in param_lists]), str(ctx.ID(1).getText()) if ctx.INHERIT() else "None", str(statement_block))

    # Visit a parse tree produced by MT22Parser#param_lists.
    def visitParam_lists(self, ctx: MT22Parser.Param_listsContext):
        if ctx.getChildCount() == 3:
            param_list = [self.visit(ctx.param_list())]
            param_lists = self.visit(ctx.param_lists())
            return param_list + param_lists
        else:
            return [self.visit(ctx.param_list())]

    # Visit a parse tree produced by MT22Parser#param_list.
    def visitParam_list(self, ctx: MT22Parser.Param_listContext):
        idlist = self.visit(ctx.idlist())
        var_type = self.visit(ctx.var_type())

        return "{}{}Param({}, {})".format("Inherit" if ctx.INHERIT() else "", "Out" if ctx.OUT() else "", ", ".join([str(id) for id in idlist]), str(var_type))

    # Visit a parse tree produced by MT22Parser#func_type.

    def visitFunc_type(self, ctx: MT22Parser.Func_typeContext):
        if ctx.VOID():
            return VoidType()
        else:
            return self.visit(ctx.var_type())

        return "FuncDecl({}, {}, [{}], {}, {})".format(self.name, str(self.return_type), ", ".join([str(param) for param in self.params]), self.inherit if self.inherit else "None", str(self.body))

    # Visit a parse tree produced by MT22Parser#var_type.
    def visitVar_type(self, ctx: MT22Parser.Var_typeContext):
        if ctx.AUTO():
            return AutoType()
        else:
            return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#booleanlit.
    def visitBooleanlit(self, ctx: MT22Parser.BooleanlitContext):
        return "BooleanLit({})".format("True" if ctx.TRUE() else "False")

    # Visit a parse tree produced by MT22Parser#indexed_array.

    def visitIndexed_array(self, ctx: MT22Parser.Indexed_arrayContext):
        list_exp = self.visit(ctx.list_exp())

        return "ArrayLit([{}])".format(", ".join([str(exp) for exp in list_exp]))

    # Visit a parse tree produced by MT22Parser#primitive_type.
    def visitPrimitive_type(self, ctx: MT22Parser.Primitive_typeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BooleanType()

    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        dimensions = self.visit(ctx.dimensions())
        primitive_type = self.visit(ctx.primitive_type())
        return "ArrayType([{}], {})".format(", ".join([str(dimen) for dimen in dimensions]), str(primitive_type))

    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        if ctx.getChildCount() == 3:  # 2
            ints = [ctx.INTEGER_LIT().getText()]
            dimensions = self.visit(ctx.dimensions())
            return ints + dimensions
        else:
            return [ctx.INTEGER_LIT().getText()]

    # Visit a parse tree produced by MT22Parser#index_operators.
    def visitIndex_operators(self, ctx: MT22Parser.Index_operatorsContext):
        id = ctx.ID().getText()
        list_exp = self.visit(ctx.list_exp())
        return "ArrayCell({}, [{}])".format(Id(id), ", ".join([str(expr) for expr in list_exp]))

    # Visit a parse tree produced by MT22Parser#func_call.

    def visitFunc_call(self, ctx: MT22Parser.Func_callContext):
        id = ctx.ID().getText()
        list_exp = self.visit(ctx.list_exp()) if ctx.list_exp() else []
        return "FuncCall({}, [{}])".format(id, ", ".join([str(expr) for expr in list_exp]))

    # Visit a parse tree produced by MT22Parser#exp.

    def visitExp(self, ctx: MT22Parser.ExpContext):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        else:
            return self.visit(ctx.exp1(0))

    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx: MT22Parser.Exp1Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        else:
            return self.visit(ctx.exp2(0))

    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx: MT22Parser.Exp2Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        else:
            return self.visit(ctx.exp3())

    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx: MT22Parser.Exp3Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp4())

    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx: MT22Parser.Exp4Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        else:
            return self.visit(ctx.exp5())

    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx: MT22Parser.Exp5Context):
        # exp5: THAN exp5 | exp6;
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.exp5()))
        else:
            return self.visit(ctx.exp6())

    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx: MT22Parser.Exp6Context):
        # exp6: SUB exp6 | exp7;
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp7())

    # Visit a parse tree produced by MT22Parser#exp7.
    def visitExp7(self, ctx: MT22Parser.Exp7Context):
        # exp7: exp8 LSB exp RSB | exp8;
        # if ctx.index_exp():
        #     return self.visit(ctx.index_exp())
        # if ctx.getChildCount() == 2:
        #    return self.visit(ctx.operands()) + self.visit(ctx.postfix_array_exp())
        if ctx.getChildCount() == 4:
            exp = self.visit(ctx.exp()) if type(
                self.visit(ctx.exp())) == type(list()) else [self.visit(ctx.exp())]
            return "ArrayCell({}, [{}])".format(self.visit(ctx.exp7()), ", ".join([str(e) for e in exp]))

            # ArrayCell(self.visit(ctx.exp7()), self.visit(ctx.exp()) if type(
            #     self.visit(ctx.exp())) == type(list()) else [self.visit(ctx.exp())])
        else:
            return self.visit(ctx.exp8())

    # Visit a parse tree produced by MT22Parser#exp8.
    def visitExp8(self, ctx: MT22Parser.Exp8Context):
        # exp11: LB exp RB | operands ;
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp())
        else:
            return self.visit(ctx.operands())

    # Visit a parse tree produced by MT22Parser#operands.
    def visitOperands(self, ctx: MT22Parser.OperandsContext):
        if ctx.INTEGER_LIT():
            return IntegerLit(int(ctx.INTEGER_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLit(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLit(str(ctx.STRING_LIT().getText()))
        elif ctx.ID():
            return "Id({})".format(ctx.ID().getText())  # ctx.ID().getText()
        else:
            return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#statement_assignment.
    def visitStatement_assignment(self, ctx: MT22Parser.Statement_assignmentContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.exp())

        return "AssignStmt({}, {})".format(str(lhs), exp)
        # return AssignStmt(lhs, exp)

    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.ID():
            return "Id({})".format(ctx.ID().getText())
        else:
            return self.visit(ctx.index_operators())

    # Visit a parse tree produced by MT22Parser#statement_if.
    def visitStatement_if(self, ctx: MT22Parser.Statement_ifContext):
        exp, true_false_statement = self.visit(ctx.if0())
        return "IfStmt({}, {}{})".format(str(exp), str(true_false_statement), ", " + self.visit(ctx.if1()))
        # return IfStmt(exp , true_false_statement, self.visit(ctx.if1()))

    # Visit a parse tree produced by MT22Parser#if0.

    def visitIf0(self, ctx: MT22Parser.If0Context):
        exp = self.visit(ctx.exp())
        true_false_statement = self.visit(ctx.true_false_statement())
        return exp, true_false_statement

    # Visit a parse tree produced by MT22Parser#if1.
    def visitIf1(self, ctx: MT22Parser.If1Context):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.true_false_statement())
        else:
            return ""

    # Visit a parse tree produced by MT22Parser#statement_for.
    def visitStatement_for(self, ctx: MT22Parser.Statement_forContext):
        id = ctx.ID().getText()
        exp1 = self.visit(ctx.exp(0))
        exp2 = self.visit(ctx.exp(1))
        exp3 = self.visit(ctx.exp(2))
        true_false_statement = self.visit(ctx.true_false_statement())

        return "ForStmt({}, {}, {}, {})".format(str("AssignStmt({}, {})".format("Id({})".format(ctx.ID().getText()), exp1)), str(exp2), str(exp3), str(true_false_statement))
        # return ForStmt(AssignStmt(id, exp1), exp2, exp3, true_false_statement)

    # Visit a parse tree produced by MT22Parser#statement_while.
    def visitStatement_while(self, ctx: MT22Parser.Statement_whileContext):
        exp = self.visit(ctx.exp())
        true_false_statement = self.visit(ctx.true_false_statement())
        return "WhileStmt({}, {})".format(str(exp), str(true_false_statement))

    # Visit a parse tree produced by MT22Parser#true_false_statement.
    def visitTrue_false_statement(self, ctx: MT22Parser.True_false_statementContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#statement_do_while.
    def visitStatement_do_while(self, ctx: MT22Parser.Statement_do_whileContext):
        exp = self.visit(ctx.exp())
        statement_block = self.visit(ctx.statement_block())
        return "DoWhileStmt({}, {})".format(str(exp), str(statement_block))

    # Visit a parse tree produced by MT22Parser#statement_break.
    def visitStatement_break(self, ctx: MT22Parser.Statement_breakContext):
        return "BreakStmt()"

    # Visit a parse tree produced by MT22Parser#statement_continue.
    def visitStatement_continue(self, ctx: MT22Parser.Statement_continueContext):
        return "ContinueStmt()"

    # Visit a parse tree produced by MT22Parser#statement_return.
    def visitStatement_return(self, ctx: MT22Parser.Statement_returnContext):
        return "ReturnStmt({})".format(str(self.visit(ctx.exp())) if ctx.exp() else "")

    # Visit a parse tree produced by MT22Parser#statement_call.

    def visitStatement_call(self, ctx: MT22Parser.Statement_callContext):
        id = ctx.ID().getText()
        if ctx.list_exp():
            list_exp = self.visit(ctx.list_exp())
            return "CallStmt({}, {})".format(id, ", ".join([str(expr) for expr in list_exp]))
            # return CallStmt(id, ", ".join([str(expr) for expr in list_exp]))
        else:
            return CallStmt(id)

        # return ["CallStmt({}, {})".format(id, ", ".join([str(expr) for expr in self.visit(ctx.list_exp())]))]

        # return "CallStmt({}, {})".format(self.name, ", ".join([str(expr) for expr in self.args]))

    # Visit a parse tree produced by MT22Parser#statement_block.

    def visitStatement_block(self, ctx: MT22Parser.Statement_blockContext):
        if ctx.bodymethods():
            return "BlockStmt([{}])".format(", ".join([str(body) for body in self.visit(ctx.bodymethods())]))
        else:
            return "BlockStmt([])"

    # Visit a parse tree produced by MT22Parser#bodymethods.

    def visitBodymethods(self, ctx: MT22Parser.BodymethodsContext):
        if ctx.getChildCount() == 2:
            bodymethod = [self.visit(ctx.bodymethod())]
            bodymethods = self.visit(ctx.bodymethods())
            return bodymethod + bodymethods
        else:
            return [self.visit(ctx.getChild(0))]

    # Visit a parse tree produced by MT22Parser#bodymethod.

    def visitBodymethod(self, ctx: MT22Parser.BodymethodContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#instructions.
    def visitInstructions(self, ctx: MT22Parser.InstructionsContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#instruction_line.
    def visitInstruction_line(self, ctx: MT22Parser.Instruction_lineContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#instruction_block.
    def visitInstruction_block(self, ctx: MT22Parser.Instruction_blockContext):
        return self.visit(ctx.getChild(0))

    # def visitSpecial_function(self, ctx: MT22Parser.Special_functionContext):
    #     return self.visit(ctx.getChild(0))

    # # Visit a parse tree produced by MT22Parser#readinteger.
    # def visitReadinteger(self, ctx: MT22Parser.ReadintegerContext):
    #     return ""
    #     return 'readInteger()'

    # # Visit a parse tree produced by MT22Parser#printinteger.
    # def visitPrintinteger(self, ctx: MT22Parser.PrintintegerContext):
    #     # return ""
    #     # return ["CallStmt(printInteger({}))".format(str(self.visit(ctx.exp())))]
    #     return ["CallStmt({}, {})".format("printInteger", ", ".join([str(expr) for expr in self.visit(ctx.list_exp())]))]

    # # Visit a parse tree produced by MT22Parser#readfloat.
    # def visitReadfloat(self, ctx: MT22Parser.ReadfloatContext):
    #     return ""
    #     return "readFloat()"

    # # Visit a parse tree produced by MT22Parser#writefloat.
    # def visitWritefloat(self, ctx: MT22Parser.WritefloatContext):
    #     return ""
    #     return "writeFloat({})".format(str(ctx.exp()))

    # # Visit a parse tree produced by MT22Parser#readboolean.
    # def visitReadboolean(self, ctx: MT22Parser.ReadbooleanContext):
    #     return ""
    #     return "readBoolean()"

    # # Visit a parse tree produced by MT22Parser#printboolean.
    # def visitPrintboolean(self, ctx: MT22Parser.PrintbooleanContext):
    #     return ""
    #     return "printBoolean({})".format(str(ctx.exp()))

    # # Visit a parse tree produced by MT22Parser#readstring.
    # def visitReadstring(self, ctx: MT22Parser.ReadstringContext):
    #     return ""
    #     return "readString()"

    # # Visit a parse tree produced by MT22Parser#printstring.
    # def visitPrintstring(self, ctx: MT22Parser.PrintstringContext):
    #     return ""
    #     return "printString({})".format(str(ctx.exp()))

    # # Visit a parse tree produced by MT22Parser#super_function.
    # def visitSuper_function(self, ctx: MT22Parser.Super_functionContext):
    #     return ""
    #     return "super({})".format(str(ctx.list_exp()))

    # # Visit a parse tree produced by MT22Parser#preventdefault.
    # def visitPreventdefault(self, ctx: MT22Parser.PreventdefaultContext):
    #     return ""
    #     return "preventDefault()"
