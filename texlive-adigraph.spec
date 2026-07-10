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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides the means to easily draw augmenting oriented
graphs, as well as cuts on them, to demonstrate steps of algorithms for
solving max-flow min-cut problems. This package requires the other LaTeX
packages fp, xparse, xstring, and TikZ (in particular the TikZ calc
library).

