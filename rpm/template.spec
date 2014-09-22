Name:           ros-indigo-openrtm-aist
Version:        1.1.0
Release:        14%{?dist}
Summary:        ROS openrtm_aist package

Group:          Development/Libraries
License:        EPL
URL:            http://ros.org/wiki/openrtm_aist
Source0:        %{name}-%{version}.tar.gz

Requires:       libuuid-devel
Requires:       omniORB
Requires:       omniORB-devel
Requires:       omniORB-servers
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libuuid-devel
BuildRequires:  omniORB
BuildRequires:  omniORB-devel
BuildRequires:  omniORB-servers
BuildRequires:  pkgconfig

%description
This package represents OpenRTM-aist that's built within ROS eco system.
Although being ROS-agnostic by itself, you can use this via ROS together with
the packages in rtmros_common that bridge between two framework. OpenRTM-aist is
an RT-Middleware-baseed, component-oriented software platform to robotics
development that is made and maintained in AIST (National Institute of Advanced
Industrial Science and Technology) in Japan (excerpts from here) Its development
is happening at openrtm.org/pub/OpenRTM-aist. The repository listed below is
where the development of its ROS wrapper happening.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Sep 22 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-14
- Autogenerated by Bloom

* Wed Sep 17 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-8
- Autogenerated by Bloom

* Wed Sep 10 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-2
- Autogenerated by Bloom

* Tue Sep 09 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-0
- Autogenerated by Bloom

* Tue Sep 09 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-1
- Autogenerated by Bloom

* Thu Sep 18 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-10
- Autogenerated by Bloom

* Thu Sep 18 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-11
- Autogenerated by Bloom

* Thu Sep 18 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-9
- Autogenerated by Bloom

* Thu Sep 11 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-4
- Autogenerated by Bloom

* Thu Sep 11 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-5
- Autogenerated by Bloom

* Thu Sep 11 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-3
- Autogenerated by Bloom

* Fri Sep 19 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-12
- Autogenerated by Bloom

* Fri Sep 19 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-13
- Autogenerated by Bloom

* Fri Sep 12 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-6
- Autogenerated by Bloom

* Fri Sep 12 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-7
- Autogenerated by Bloom

