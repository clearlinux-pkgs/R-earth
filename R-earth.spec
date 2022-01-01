#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-earth
Version  : 5.3.1
Release  : 51
URL      : https://cran.r-project.org/src/contrib/earth_5.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/earth_5.3.1.tar.gz
Summary  : Multivariate Adaptive Regression Splines
Group    : Development/Tools
License  : GPL-3.0
Requires: R-earth-lib = %{version}-%{release}
Requires: R-Formula
Requires: R-TeachingDemos
Requires: R-plotmo
BuildRequires : R-Formula
BuildRequires : R-TeachingDemos
BuildRequires : R-plotmo
BuildRequires : buildreq-R

%description
papers "Fast MARS" and "Multivariate Adaptive Regression

%package lib
Summary: lib components for the R-earth package.
Group: Libraries

%description lib
lib components for the R-earth package.


%prep
%setup -q -c -n earth
cd %{_builddir}/earth

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641005362

%install
export SOURCE_DATE_EPOCH=1641005362
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library earth
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library earth
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library earth
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc earth || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/earth/DESCRIPTION
/usr/lib64/R/library/earth/INDEX
/usr/lib64/R/library/earth/Meta/Rd.rds
/usr/lib64/R/library/earth/Meta/data.rds
/usr/lib64/R/library/earth/Meta/features.rds
/usr/lib64/R/library/earth/Meta/hsearch.rds
/usr/lib64/R/library/earth/Meta/links.rds
/usr/lib64/R/library/earth/Meta/nsInfo.rds
/usr/lib64/R/library/earth/Meta/package.rds
/usr/lib64/R/library/earth/NAMESPACE
/usr/lib64/R/library/earth/NEWS
/usr/lib64/R/library/earth/R/earth
/usr/lib64/R/library/earth/R/earth.rdb
/usr/lib64/R/library/earth/R/earth.rdx
/usr/lib64/R/library/earth/data/Rdata.rdb
/usr/lib64/R/library/earth/data/Rdata.rds
/usr/lib64/R/library/earth/data/Rdata.rdx
/usr/lib64/R/library/earth/doc/Auto-linpreds-example.pdf
/usr/lib64/R/library/earth/doc/earth-notes.pdf
/usr/lib64/R/library/earth/doc/earth-varmod.pdf
/usr/lib64/R/library/earth/doc/index.html
/usr/lib64/R/library/earth/help/AnIndex
/usr/lib64/R/library/earth/help/aliases.rds
/usr/lib64/R/library/earth/help/earth.rdb
/usr/lib64/R/library/earth/help/earth.rdx
/usr/lib64/R/library/earth/help/paths.rds
/usr/lib64/R/library/earth/html/00Index.html
/usr/lib64/R/library/earth/html/R.css
/usr/lib64/R/library/earth/slowtests/README.txt
/usr/lib64/R/library/earth/slowtests/check.earth.matches.glm.R
/usr/lib64/R/library/earth/slowtests/check.models.equal.R
/usr/lib64/R/library/earth/slowtests/earth.times.R
/usr/lib64/R/library/earth/slowtests/earth.times.bat
/usr/lib64/R/library/earth/slowtests/earth.times.txt
/usr/lib64/R/library/earth/slowtests/make.bat
/usr/lib64/R/library/earth/slowtests/makeclean.bat
/usr/lib64/R/library/earth/slowtests/test.allowedfunc.R
/usr/lib64/R/library/earth/slowtests/test.allowedfunc.Rout.save
/usr/lib64/R/library/earth/slowtests/test.allowedfunc.bat
/usr/lib64/R/library/earth/slowtests/test.big.R
/usr/lib64/R/library/earth/slowtests/test.big.Rout.save
/usr/lib64/R/library/earth/slowtests/test.big.bat
/usr/lib64/R/library/earth/slowtests/test.bpairs.R
/usr/lib64/R/library/earth/slowtests/test.bpairs.Rout.save
/usr/lib64/R/library/earth/slowtests/test.bpairs.bat
/usr/lib64/R/library/earth/slowtests/test.cv.R
/usr/lib64/R/library/earth/slowtests/test.cv.Rout.save
/usr/lib64/R/library/earth/slowtests/test.cv.bat
/usr/lib64/R/library/earth/slowtests/test.earthc.c
/usr/lib64/R/library/earth/slowtests/test.earthc.clang.bat
/usr/lib64/R/library/earth/slowtests/test.earthc.gcc.bat
/usr/lib64/R/library/earth/slowtests/test.earthc.msc.bat
/usr/lib64/R/library/earth/slowtests/test.earthc.msc.mak
/usr/lib64/R/library/earth/slowtests/test.earthc.out.save
/usr/lib64/R/library/earth/slowtests/test.earthmain.clang.bat
/usr/lib64/R/library/earth/slowtests/test.earthmain.gcc.bat
/usr/lib64/R/library/earth/slowtests/test.earthmain.gcc64.bat
/usr/lib64/R/library/earth/slowtests/test.earthmain.msc.bat
/usr/lib64/R/library/earth/slowtests/test.earthmain.out.save
/usr/lib64/R/library/earth/slowtests/test.emma.R
/usr/lib64/R/library/earth/slowtests/test.emma.Rout.save
/usr/lib64/R/library/earth/slowtests/test.emma.bat
/usr/lib64/R/library/earth/slowtests/test.epilog.R
/usr/lib64/R/library/earth/slowtests/test.expand.bpairs.R
/usr/lib64/R/library/earth/slowtests/test.expand.bpairs.Rout.save
/usr/lib64/R/library/earth/slowtests/test.expand.bpairs.bat
/usr/lib64/R/library/earth/slowtests/test.full.R
/usr/lib64/R/library/earth/slowtests/test.full.Rout.save
/usr/lib64/R/library/earth/slowtests/test.full.bat
/usr/lib64/R/library/earth/slowtests/test.glm.R
/usr/lib64/R/library/earth/slowtests/test.glm.Rout.save
/usr/lib64/R/library/earth/slowtests/test.glm.bat
/usr/lib64/R/library/earth/slowtests/test.incorrect.R
/usr/lib64/R/library/earth/slowtests/test.incorrect.Rout.save
/usr/lib64/R/library/earth/slowtests/test.incorrect.bat
/usr/lib64/R/library/earth/slowtests/test.mem.R
/usr/lib64/R/library/earth/slowtests/test.mem.Rout.save
/usr/lib64/R/library/earth/slowtests/test.mem.bat
/usr/lib64/R/library/earth/slowtests/test.mods.R
/usr/lib64/R/library/earth/slowtests/test.mods.Rout.save
/usr/lib64/R/library/earth/slowtests/test.mods.bat
/usr/lib64/R/library/earth/slowtests/test.multresp.R
/usr/lib64/R/library/earth/slowtests/test.multresp.Rout.save
/usr/lib64/R/library/earth/slowtests/test.multresp.bat
/usr/lib64/R/library/earth/slowtests/test.numstab-mfpmath-387.Rout.save
/usr/lib64/R/library/earth/slowtests/test.numstab.R
/usr/lib64/R/library/earth/slowtests/test.numstab.Rout.save
/usr/lib64/R/library/earth/slowtests/test.numstab.bat
/usr/lib64/R/library/earth/slowtests/test.offset.R
/usr/lib64/R/library/earth/slowtests/test.offset.Rout.save
/usr/lib64/R/library/earth/slowtests/test.offset.bat
/usr/lib64/R/library/earth/slowtests/test.ordinal.R
/usr/lib64/R/library/earth/slowtests/test.ordinal.Rout.save
/usr/lib64/R/library/earth/slowtests/test.ordinal.bat
/usr/lib64/R/library/earth/slowtests/test.plotd.R
/usr/lib64/R/library/earth/slowtests/test.plotd.Rout.save
/usr/lib64/R/library/earth/slowtests/test.plotd.bat
/usr/lib64/R/library/earth/slowtests/test.pmethod.cv.R
/usr/lib64/R/library/earth/slowtests/test.pmethod.cv.Rout.save
/usr/lib64/R/library/earth/slowtests/test.pmethod.cv.bat
/usr/lib64/R/library/earth/slowtests/test.prolog.R
/usr/lib64/R/library/earth/slowtests/test.varmod.R
/usr/lib64/R/library/earth/slowtests/test.varmod.Rout.save
/usr/lib64/R/library/earth/slowtests/test.varmod.bat
/usr/lib64/R/library/earth/slowtests/test.varmod.mgcv.R
/usr/lib64/R/library/earth/slowtests/test.varmod.mgcv.Rout.save
/usr/lib64/R/library/earth/slowtests/test.varmod.mgcv.bat
/usr/lib64/R/library/earth/slowtests/test.weights.R
/usr/lib64/R/library/earth/slowtests/test.weights.Rout.save
/usr/lib64/R/library/earth/slowtests/test.weights.bat
/usr/lib64/R/library/earth/tests/README.txt
/usr/lib64/R/library/earth/tests/test.earth.R
/usr/lib64/R/library/earth/tests/test.earth.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/earth/libs/earth.so
/usr/lib64/R/library/earth/libs/earth.so.avx2
/usr/lib64/R/library/earth/libs/earth.so.avx512
