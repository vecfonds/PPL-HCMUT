# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl.
    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl_normal.
    def visitVardecl_normal(self, ctx:MT22Parser.Vardecl_normalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl_symmetric.
    def visitVardecl_symmetric(self, ctx:MT22Parser.Vardecl_symmetricContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_exp.
    def visitList_exp(self, ctx:MT22Parser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_decl.
    def visitFunc_decl(self, ctx:MT22Parser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_lists.
    def visitParam_lists(self, ctx:MT22Parser.Param_listsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_list.
    def visitParam_list(self, ctx:MT22Parser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_type.
    def visitFunc_type(self, ctx:MT22Parser.Func_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_type.
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#booleanlit.
    def visitBooleanlit(self, ctx:MT22Parser.BooleanlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexed_array.
    def visitIndexed_array(self, ctx:MT22Parser.Indexed_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#primitive_type.
    def visitPrimitive_type(self, ctx:MT22Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_operators.
    def visitIndex_operators(self, ctx:MT22Parser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_call.
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp.
    def visitExp(self, ctx:MT22Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp7.
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp8.
    def visitExp8(self, ctx:MT22Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operands.
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_assignment.
    def visitStatement_assignment(self, ctx:MT22Parser.Statement_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_if.
    def visitStatement_if(self, ctx:MT22Parser.Statement_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if0.
    def visitIf0(self, ctx:MT22Parser.If0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if1.
    def visitIf1(self, ctx:MT22Parser.If1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_for.
    def visitStatement_for(self, ctx:MT22Parser.Statement_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_while.
    def visitStatement_while(self, ctx:MT22Parser.Statement_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#true_false_statement.
    def visitTrue_false_statement(self, ctx:MT22Parser.True_false_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_do_while.
    def visitStatement_do_while(self, ctx:MT22Parser.Statement_do_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_break.
    def visitStatement_break(self, ctx:MT22Parser.Statement_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_continue.
    def visitStatement_continue(self, ctx:MT22Parser.Statement_continueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_return.
    def visitStatement_return(self, ctx:MT22Parser.Statement_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_call.
    def visitStatement_call(self, ctx:MT22Parser.Statement_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_block.
    def visitStatement_block(self, ctx:MT22Parser.Statement_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bodymethods.
    def visitBodymethods(self, ctx:MT22Parser.BodymethodsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bodymethod.
    def visitBodymethod(self, ctx:MT22Parser.BodymethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#instructions.
    def visitInstructions(self, ctx:MT22Parser.InstructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#instruction_line.
    def visitInstruction_line(self, ctx:MT22Parser.Instruction_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#instruction_block.
    def visitInstruction_block(self, ctx:MT22Parser.Instruction_blockContext):
        return self.visitChildren(ctx)



del MT22Parser