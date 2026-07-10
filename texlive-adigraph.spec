%global tl_name adigraph
%global tl_revision 70422

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7.2
Release:	%{tl_revision}.1
Summary:	Augmenting directed graphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/adigraph
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adigraph.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adigraph.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides the means to easily draw augmenting oriented
graphs, as well as cuts on them, to demonstrate steps of algorithms for
solving max-flow min-cut problems. This package requires the other LaTeX
packages fp, xparse, xstring, and TikZ (in particular the TikZ calc
library).

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/adigraph
%dir %{_datadir}/texmf-dist/tex/latex/adigraph
%dir %{_datadir}/texmf-dist/doc/latex/adigraph/img_examples
%doc %{_datadir}/texmf-dist/doc/latex/adigraph/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/adigraph/README.md
%doc %{_datadir}/texmf-dist/doc/latex/adigraph/adigraph-large.png
%doc %{_datadir}/texmf-dist/doc/latex/adigraph/adigraph_documentation.pdf
%doc %{_datadir}/texmf-dist/doc/latex/adigraph/adigraph_documentation.tex
%doc %{_datadir}/texmf-dist/doc/latex/adigraph/adigraph_working_test.pdf
%doc %{_datadir}/texmf-dist/doc/latex/adigraph/adigraph_working_test.tex
%doc %{_datadir}/texmf-dist/doc/latex/adigraph/img_examples/example_0.jpg
%doc %{_datadir}/texmf-dist/doc/latex/adigraph/img_examples/example_1.jpg
%doc %{_datadir}/texmf-dist/doc/latex/adigraph/img_examples/example_2.jpg
%doc %{_datadir}/texmf-dist/doc/latex/adigraph/img_examples/example_3.jpg
%doc %{_datadir}/texmf-dist/doc/latex/adigraph/img_examples/pyadigraph.png
%{_datadir}/texmf-dist/tex/latex/adigraph/adigraph.sty
