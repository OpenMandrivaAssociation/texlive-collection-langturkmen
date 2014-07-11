# revision 17578
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langturkmen
Epoch:		1
Version:	20120224
Release:	7
Summary:	Turkmen
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langturkmen.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-turkmen
Requires:	texlive-hyphen-turkmen
Requires:	texlive-collection-basic

%description
Support for typesetting Turkmen.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780457
- Update to latest release.
- Import texlive-collection-langturkmen
- Import texlive-collection-langturkmen

