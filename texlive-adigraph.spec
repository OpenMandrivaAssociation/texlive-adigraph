Name:		texlive-adigraph
Version:	49862
Release:	2
Summary:	Augmenting directed graphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/adigraph
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adigraph.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adigraph.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides the means to easily draw augmenting
oriented graphs, as well as cuts on them, to demonstrate steps
of algorithms for solving max-flow min-cut problems. This
package requires the other LaTeX packages fp, xparse, xstring,
and TikZ (in particular the TikZ calc library).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/adigraph
%doc %{_texmfdistdir}/doc/latex/adigraph

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
