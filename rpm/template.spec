Name:           ros-indigo-carl-interactive-manipulation
Version:        0.0.22
Release:        0%{?dist}
Summary:        ROS carl_interactive_manipulation package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/carl_bot
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-carl-moveit
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-interactive-markers
Requires:       ros-indigo-move-base-msgs
Requires:       ros-indigo-rail-pick-and-place-msgs
Requires:       ros-indigo-rail-segmentation
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-urdf
Requires:       ros-indigo-visualization-msgs
Requires:       ros-indigo-wpi-jaco-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-carl-moveit
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-interactive-markers
BuildRequires:  ros-indigo-move-base-msgs
BuildRequires:  ros-indigo-rail-pick-and-place-msgs
BuildRequires:  ros-indigo-rail-segmentation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-urdf
BuildRequires:  ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-wpi-jaco-msgs

%description
Interactive Manipulation for CARL

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Apr 03 2015 David Kent <davidkent@wpi.edu> - 0.0.22-0
- Autogenerated by Bloom

* Tue Mar 31 2015 David Kent <davidkent@wpi.edu> - 0.0.21-0
- Autogenerated by Bloom

* Tue Mar 31 2015 David Kent <davidkent@wpi.edu> - 0.0.20-0
- Autogenerated by Bloom

* Fri Mar 27 2015 David Kent <davidkent@wpi.edu> - 0.0.19-0
- Autogenerated by Bloom

* Fri Mar 27 2015 David Kent <davidkent@wpi.edu> - 0.0.18-0
- Autogenerated by Bloom

* Tue Mar 24 2015 David Kent <davidkent@wpi.edu> - 0.0.17-0
- Autogenerated by Bloom

* Tue Feb 17 2015 David Kent <davidkent@wpi.edu> - 0.0.16-0
- Autogenerated by Bloom

* Tue Feb 10 2015 David Kent <davidkent@wpi.edu> - 0.0.15-0
- Autogenerated by Bloom

* Fri Feb 06 2015 David Kent <davidkent@wpi.edu> - 0.0.14-0
- Autogenerated by Bloom

* Wed Jan 21 2015 David Kent <davidkent@wpi.edu> - 0.0.13-0
- Autogenerated by Bloom

* Mon Jan 19 2015 David Kent <davidkent@wpi.edu> - 0.0.12-0
- Autogenerated by Bloom

* Thu Dec 18 2014 David Kent <davidkent@wpi.edu> - 0.0.11-0
- Autogenerated by Bloom

