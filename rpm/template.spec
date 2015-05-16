Name:           ros-indigo-naoqi-libqicore
Version:        2.3.1
Release:        2%{?dist}
Summary:        ROS naoqi_libqicore package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-naoqi-libqi
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-naoqi-libqi

%description
Aldebaran's libqicore: a layer on top of libqi

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
* Sat May 16 2015 Mikael Arguedas <mikael.arguedas@gmail.com> - 2.3.1-2
- Autogenerated by Bloom

* Fri May 15 2015 Mikael Arguedas <mikael.arguedas@gmail.com> - 2.3.1-1
- Autogenerated by Bloom

* Fri May 15 2015 Mikael Arguedas <mikael.arguedas@gmail.com> - 2.3.1-0
- Autogenerated by Bloom

