Summary:	GNU Artanis web-framework
Summary(pl.UTF-8):	GNU Artanis - szkielet WWW
Name:		artanis
Version:	0.6
Release:	1
License:	GPL v3+, LGPL v3+
Group:		Applications/Networking
Source0:	https://ftp.gnu.org/gnu/artanis/%{name}-%{version}.tar.bz2
# Source0-md5:	edafd8a97c8fcb3220320c75306fef6e
URL:		http://www.gnu.org/software/artanis/
BuildRequires:	guile-curl
BuildRequires:	guile-devel >= 5:3.0
BuildRequires:	guile-devel < 5:3.2
Requires:	guile >= 5:3.0
Requires:	guile-curl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Artanis aims to be a web application framework for Scheme.

%description -l pl.UTF-8
GNU Artanis to szkielet aplikacji WWW dla Scheme.

%package -n bash-completion-artanis
Summary:	Bash completion for artanis commands
Summary(pl.UTF-8):	Bashowe dopełnianie poleceń artanis
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}

%description -n bash-completion-artanis
Bash completion for artanis commands.

%description -n bash-completion-artanis -l pl.UTF-8
Bashowe dopełnianie poleceń artanis.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT{/bin,%{_prefix}/bin}

%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/artanis/.gitkeep

install -d $RPM_BUILD_ROOT%{bash_compdir}
cp -p build-aux/show-artanis-cmds.sh $RPM_BUILD_ROOT%{bash_compdir}/artanis

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS NEWS README.md SECURITY_WARNING THANKS TODO
%attr(755,root,root) %{_bindir}/art
%dir %{_sysconfdir}/artanis
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/artanis/artanis.conf
%dir %{_sysconfdir}/artanis/pages
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/artanis/pages/*.html
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/artanis/pages/warn-the-client.tpl
%{_libdir}/guile/?.?/site-ccache/artanis
%{_datadir}/guile/site/?.?/artanis

%files -n bash-completion-artanis
%defattr(644,root,root,755)
%{bash_compdir}/artanis
