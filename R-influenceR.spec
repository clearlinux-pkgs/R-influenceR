#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-influenceR
Version  : 0.1.0
Release  : 8
URL      : https://cran.r-project.org/src/contrib/influenceR_0.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/influenceR_0.1.0.tar.gz
Summary  : Software Tools to Quantify Structural Importance of Nodes in a
Group    : Development/Tools
License  : GPL-2.0
Requires: R-influenceR-lib = %{version}-%{release}
Requires: R-igraph
BuildRequires : R-igraph
BuildRequires : buildreq-R

%description
Included are functions to compute betweenness centrality (by utilizing Madduri and Bader's
    SNAP library), implementations of Burt's constraint and effective
    network size (ENS) metrics, Borgatti's algorithm to identify key players, and Valente's
    bridging metric. On Unix systems, the betweenness, Key Players, and
    bridging implementations are parallelized with OpenMP, which may run
    faster on systems which have OpenMP configured.

%package lib
Summary: lib components for the R-influenceR package.
Group: Libraries

%description lib
lib components for the R-influenceR package.


%prep
%setup -q -c -n influenceR
cd %{_builddir}/influenceR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589578494

%install
export SOURCE_DATE_EPOCH=1589578494
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library influenceR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library influenceR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library influenceR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc influenceR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/influenceR/DESCRIPTION
/usr/lib64/R/library/influenceR/INDEX
/usr/lib64/R/library/influenceR/Meta/Rd.rds
/usr/lib64/R/library/influenceR/Meta/features.rds
/usr/lib64/R/library/influenceR/Meta/hsearch.rds
/usr/lib64/R/library/influenceR/Meta/links.rds
/usr/lib64/R/library/influenceR/Meta/nsInfo.rds
/usr/lib64/R/library/influenceR/Meta/package.rds
/usr/lib64/R/library/influenceR/NAMESPACE
/usr/lib64/R/library/influenceR/R/influenceR
/usr/lib64/R/library/influenceR/R/influenceR.rdb
/usr/lib64/R/library/influenceR/R/influenceR.rdx
/usr/lib64/R/library/influenceR/help/AnIndex
/usr/lib64/R/library/influenceR/help/aliases.rds
/usr/lib64/R/library/influenceR/help/influenceR.rdb
/usr/lib64/R/library/influenceR/help/influenceR.rdx
/usr/lib64/R/library/influenceR/help/paths.rds
/usr/lib64/R/library/influenceR/html/00Index.html
/usr/lib64/R/library/influenceR/html/R.css
/usr/lib64/R/library/influenceR/tests/testthat.R
/usr/lib64/R/library/influenceR/tests/testthat/flo_results.RData
/usr/lib64/R/library/influenceR/tests/testthat/test_metrics.R
/usr/lib64/R/library/influenceR/tests/testthat/test_reference.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/influenceR/libs/influenceR.so
/usr/lib64/R/library/influenceR/libs/influenceR.so.avx2
/usr/lib64/R/library/influenceR/libs/influenceR.so.avx512
