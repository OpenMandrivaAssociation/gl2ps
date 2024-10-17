%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	An OpenGL to PostScript printing library
Name:		gl2ps
Version:	1.4.2
Release:	2
License:	LGPLv2+ or GL2PS
Group:		System/Libraries
URL:		https://www.geuz.org/%{name}/
Source0:	http://geuz.org/%{name}/src/%{name}-%{version}.tgz

BuildRequires:	cmake
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(glut)

%description
GL2PS is a C library providing high quality vector output for any OpenGL
application. The main difference between GL2PS and other similar libraries
(see section 7) is the use of sorting algorithms capable of handling
intersecting and stretched polygons, as well as non manifold objects.
GL2PS provides advanced smooth shading and text rendering, culling of
invisible primitives, mixed vector/bitmap output, and much more...

GL2PS can currently create PostScript (PS), Encapsulated PostScript (EPS),
Portable Document Format (PDF) and Scalable Vector Graphics (SVG) files, as
well as LaTeX files for the text fragments. GL2PS also provides limited,
experimental support for Portable LaTeX Graphics (PGF). Adding new vector
output formats should be relatively easy; you can also use the excellent
pstoedit program to transform the PostScript files generated by GL2PS into
many other vector formats such as xfig, cgm, wmf, etc. 

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	An OpenGL to PostScript printing library
Group:		System/Libraries

%description -n %{libname}
application. The main difference between GL2PS and other similar libraries
(see section 7) is the use of sorting algorithms capable of handling
intersecting and stretched polygons, as well as non manifold objects.
GL2PS provides advanced smooth shading and text rendering, culling of
invisible primitives, mixed vector/bitmap output, and much more...

GL2PS can currently create PostScript (PS), Encapsulated PostScript (EPS),
Portable Document Format (PDF) and Scalable Vector Graphics (SVG) files, as
well as LaTeX files for the text fragments. GL2PS also provides limited,
experimental support for Portable LaTeX Graphics (PGF). Adding new vector
output formats should be relatively easy; you can also use the excellent
pstoedit program to transform the PostScript files generated by GL2PS into
many other vector formats such as xfig, cgm, wmf, etc. 


%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*
%doc README.txt
%doc COPYING.GL2PS
%doc COPYING.LGPL

#--------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the SRTP library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains header files and development libraries needed to
develop programs using the GL2PS library.

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%doc gl2psTest*.c
%doc gl2ps.pdf
%doc README.txt
%doc COPYING.GL2PS
%doc COPYING.LGPL

#%{_libdir}/pkgconfig/lib%{name}.pc

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

# remove static lib
rm -f %{buildroot}%{_libdir}/lib%{name}.a

# remove unused docs
rm -r %{buildroot}%{_docdir}/%{name}
