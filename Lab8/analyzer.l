%{

#include <stdio.h>

%}

%option noyywrap

LETTER [a-z]

%%

{LETTER}+ {
    printf("found word %s \n", yytext);
}

%%

int main() {
    // yyin = fopen("word", "r");
    int result = yylex();
    if (result == 0)
        printf("A mers :))\n");
    return 0;
}