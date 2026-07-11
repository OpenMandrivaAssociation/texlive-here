%global tl_name here
%global tl_revision 78348

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Emulation of obsolete package for here floats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/here
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/here.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/here.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides the H option for floats in LaTeX to signify that the
environment is not really a float (and should therefore be placed "here"
and not float at all). The package emulates an older package of the same
name, which has long been suppressed by its author. The job is done by
nothing more than loading the float package, which has long provided the
option in an acceptable framework.

