%module(directors="1", allprotected="1") pyepanet2
%feature("director");

%feature("autodoc", "1");

%{
    #include <epanet2.h>
%}

%include <epanet2.h>
