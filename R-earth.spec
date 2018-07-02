#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-earth
Version  : 4.6.3
Release  : 13
URL      : https://cran.r-project.org/src/contrib/earth_4.6.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/earth_4.6.3.tar.gz
Summary  : Multivariate Adaptive Regression Splines
Group    : Development/Tools
License  : GPL-3.0
Requires: R-earth-lib
Requires: R-TeachingDemos
Requires: R-gam
Requires: R-leaps
Requires: R-mda
Requires: R-plotmo
BuildRequires : R-TeachingDemos
BuildRequires : R-gam
BuildRequires : R-leaps
BuildRequires : R-mda
BuildRequires : R-plotmo
BuildRequires : clr-R-helpers

%description
papers "Fast MARS" and "Multivariate Adaptive Regression

%package lib
Summary: lib components for the R-earth package.
Group: Libraries

%description lib
lib components for the R-earth package.


%prep
%setup -q -c -n earth

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525795285

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1525795285
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library earth
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library earth
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library earth
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library earth|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/earth/data/etitanic.rda
/usr/lib64/R/library/earth/data/ozone1.rda
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
/usr/lib64/R/library/earth/libs/symbols.rds
/usr/lib64/R/library/earth/slowtests/README.txt
/usr/lib64/R/library/earth/slowtests/check.models.equal.R
/usr/lib64/R/library/earth/slowtests/earth.times.R
/usr/lib64/R/library/earth/slowtests/earth.times.bat
/usr/lib64/R/library/earth/slowtests/earth.times.txt
/usr/lib64/R/library/earth/slowtests/make.bat
/usr/lib64/R/library/earth/slowtests/test.big.R
/usr/lib64/R/library/earth/slowtests/test.big.Rout.save
/usr/lib64/R/library/earth/slowtests/test.big.bat
/usr/lib64/R/library/earth/slowtests/test.cv.R
/usr/lib64/R/library/earth/slowtests/test.cv.Rout.save
/usr/lib64/R/library/earth/slowtests/test.cv.bat
/usr/lib64/R/library/earth/slowtests/test.earthc.bat
/usr/lib64/R/library/earth/slowtests/test.earthc.c
/usr/lib64/R/library/earth/slowtests/test.earthc.mak
/usr/lib64/R/library/earth/slowtests/test.earthc.out.save
/usr/lib64/R/library/earth/slowtests/test.earthmain.clang.bat
/usr/lib64/R/library/earth/slowtests/test.earthmain.gcc.bat
/usr/lib64/R/library/earth/slowtests/test.earthmain.gcc64.bat
/usr/lib64/R/library/earth/slowtests/test.earthmain.out.save
/usr/lib64/R/library/earth/slowtests/test.earthmain.vc.bat
/usr/lib64/R/library/earth/slowtests/test.full.R
/usr/lib64/R/library/earth/slowtests/test.full.Rout.save
/usr/lib64/R/library/earth/slowtests/test.full.bat
/usr/lib64/R/library/earth/slowtests/test.glm.R
/usr/lib64/R/library/earth/slowtests/test.glm.Rout.save
/usr/lib64/R/library/earth/slowtests/test.glm.bat
/usr/lib64/R/library/earth/slowtests/test.incorrect.R
/usr/lib64/R/library/earth/slowtests/test.incorrect.Rout.save
/usr/lib64/R/library/earth/slowtests/test.incorrect.bat
/usr/lib64/R/library/earth/slowtests/test.mods.R
/usr/lib64/R/library/earth/slowtests/test.mods.Rout.save
/usr/lib64/R/library/earth/slowtests/test.mods.bat
/usr/lib64/R/library/earth/slowtests/test.plotd.R
/usr/lib64/R/library/earth/slowtests/test.plotd.Rout.save
/usr/lib64/R/library/earth/slowtests/test.plotd.bat
/usr/lib64/R/library/earth/slowtests/test.pmethod.cv.R
/usr/lib64/R/library/earth/slowtests/test.pmethod.cv.Rout.save
/usr/lib64/R/library/earth/slowtests/test.pmethod.cv.bat
/usr/lib64/R/library/earth/slowtests/test.varmod.R
/usr/lib64/R/library/earth/slowtests/test.varmod.Rout.save
/usr/lib64/R/library/earth/slowtests/test.varmod.bat
/usr/lib64/R/library/earth/slowtests/test.varmod.mgcv.R
/usr/lib64/R/library/earth/slowtests/test.varmod.mgcv.Rout.save
/usr/lib64/R/library/earth/slowtests/test.varmod.mgcv.bat
/usr/lib64/R/library/earth/slowtests/test.weights.R
/usr/lib64/R/library/earth/slowtests/test.weights.Rout.save
/usr/lib64/R/library/earth/slowtests/test.weights.bat

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/earth/libs/earth.so
/usr/lib64/R/library/earth/libs/earth.so.avx2
/usr/lib64/R/library/earth/libs/earth.so.avx512
