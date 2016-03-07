// Generated by gencpp from file vrep_common/simRosSetArrayParameterRequest.msg
// DO NOT EDIT!


#ifndef VREP_COMMON_MESSAGE_SIMROSSETARRAYPARAMETERREQUEST_H
#define VREP_COMMON_MESSAGE_SIMROSSETARRAYPARAMETERREQUEST_H


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
struct simRosSetArrayParameterRequest_
{
  typedef simRosSetArrayParameterRequest_<ContainerAllocator> Type;

  simRosSetArrayParameterRequest_()
    : parameter(0)
    , parameterValues()  {
    }
  simRosSetArrayParameterRequest_(const ContainerAllocator& _alloc)
    : parameter(0)
    , parameterValues(_alloc)  {
    }



   typedef int32_t _parameter_type;
  _parameter_type parameter;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _parameterValues_type;
  _parameterValues_type parameterValues;




  typedef boost::shared_ptr< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> const> ConstPtr;

}; // struct simRosSetArrayParameterRequest_

typedef ::vrep_common::simRosSetArrayParameterRequest_<std::allocator<void> > simRosSetArrayParameterRequest;

typedef boost::shared_ptr< ::vrep_common::simRosSetArrayParameterRequest > simRosSetArrayParameterRequestPtr;
typedef boost::shared_ptr< ::vrep_common::simRosSetArrayParameterRequest const> simRosSetArrayParameterRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace vrep_common

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/jade/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/jade/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/jade/share/geometry_msgs/cmake/../msg'], 'vrep_common': ['/home/etudiant/CelluleFlexible/catkin_ws/src/vrep_common/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5d2ff3aea97ae3d86be296a72ec9a583";
  }

  static const char* value(const ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5d2ff3aea97ae3d8ULL;
  static const uint64_t static_value2 = 0x6be296a72ec9a583ULL;
};

template<class ContainerAllocator>
struct DataType< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vrep_common/simRosSetArrayParameterRequest";
  }

  static const char* value(const ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
\n\
\n\
\n\
int32 parameter\n\
float32[] parameterValues\n\
";
  }

  static const char* value(const ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.parameter);
      stream.next(m.parameterValues);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct simRosSetArrayParameterRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vrep_common::simRosSetArrayParameterRequest_<ContainerAllocator>& v)
  {
    s << indent << "parameter: ";
    Printer<int32_t>::stream(s, indent + "  ", v.parameter);
    s << indent << "parameterValues[]" << std::endl;
    for (size_t i = 0; i < v.parameterValues.size(); ++i)
    {
      s << indent << "  parameterValues[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.parameterValues[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // VREP_COMMON_MESSAGE_SIMROSSETARRAYPARAMETERREQUEST_H
