// Generated by gencpp from file vrep_common/simRosSetModelPropertyRequest.msg
// DO NOT EDIT!


#ifndef VREP_COMMON_MESSAGE_SIMROSSETMODELPROPERTYREQUEST_H
#define VREP_COMMON_MESSAGE_SIMROSSETMODELPROPERTYREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace vrep_common
{
template <class ContainerAllocator>
struct simRosSetModelPropertyRequest_
{
  typedef simRosSetModelPropertyRequest_<ContainerAllocator> Type;

  simRosSetModelPropertyRequest_()
    : handle(0)
    , propertyValue(0)  {
    }
  simRosSetModelPropertyRequest_(const ContainerAllocator& _alloc)
    : handle(0)
    , propertyValue(0)  {
    }



   typedef int32_t _handle_type;
  _handle_type handle;

   typedef int32_t _propertyValue_type;
  _propertyValue_type propertyValue;




  typedef boost::shared_ptr< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> const> ConstPtr;

}; // struct simRosSetModelPropertyRequest_

typedef ::vrep_common::simRosSetModelPropertyRequest_<std::allocator<void> > simRosSetModelPropertyRequest;

typedef boost::shared_ptr< ::vrep_common::simRosSetModelPropertyRequest > simRosSetModelPropertyRequestPtr;
typedef boost::shared_ptr< ::vrep_common::simRosSetModelPropertyRequest const> simRosSetModelPropertyRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace vrep_common

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/jade/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/jade/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/jade/share/geometry_msgs/cmake/../msg'], 'vrep_common': ['/home/etudiant/CelluleFlexible/catkin_ws/src/vrep_common/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c1dfc3d3e983651365795ed48e7ad342";
  }

  static const char* value(const ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc1dfc3d3e9836513ULL;
  static const uint64_t static_value2 = 0x65795ed48e7ad342ULL;
};

template<class ContainerAllocator>
struct DataType< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vrep_common/simRosSetModelPropertyRequest";
  }

  static const char* value(const ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
\n\
\n\
\n\
int32 handle\n\
int32 propertyValue\n\
";
  }

  static const char* value(const ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.handle);
      stream.next(m.propertyValue);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct simRosSetModelPropertyRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vrep_common::simRosSetModelPropertyRequest_<ContainerAllocator>& v)
  {
    s << indent << "handle: ";
    Printer<int32_t>::stream(s, indent + "  ", v.handle);
    s << indent << "propertyValue: ";
    Printer<int32_t>::stream(s, indent + "  ", v.propertyValue);
  }
};

} // namespace message_operations
} // namespace ros

#endif // VREP_COMMON_MESSAGE_SIMROSSETMODELPROPERTYREQUEST_H
