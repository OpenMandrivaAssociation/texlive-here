# revision 16135
# category Package
# catalog-ctan /macros/latex/contrib/here
# catalog-date 2009-11-28 09:57:52 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-here
Version:	20091128
Release:	1
Summary:	Emulation of obsolete package for "here" floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/here
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/here.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/here.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides the H option for floats in LaTeX to signify that the
environemt is not really a float (and should therefore be
placed "here" and not float at all). The package emulates an
older package of the same name, which has long been been
suppressed by its author. The job is done by nothing more than
loading the float package, which has long provided the option
in an acceptable framework.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/here/here.sty
%doc %{_texmfdistdir}/doc/latex/here/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
