#pragma once

#ifndef SIRF_ABSTRACT_IMAGE_DATA_TYPE
#define SIRF_ABSTRACT_IMAGE_DATA_TYPE

#include "sirf/common/ANumRef.h"
#include "sirf/common/DataContainer.h"

/*!
\ingroup SIRFImageDataClasses
\brief Abstract base class for SIRF image data.

*/
namespace sirf {
	class ImageData : public DataContainer
	{
	public:
		virtual ~ImageData() {}
		virtual Dimensions dimensions() const = 0; // to go to DataContainer eventually
		//virtual void get_data(void* data) const = 0;
		//virtual void set_data(const void* data) = 0;
		class Iterator {
		public:
			virtual ~Iterator() {}
			virtual Iterator& operator++() = 0;
			virtual ANumRef& operator*() = 0;
			virtual bool operator==(const Iterator&) const = 0;
			virtual bool operator!=(const Iterator&) const = 0;
		};
		class Iterator_const {
		public:
			virtual ~Iterator_const() {}
			virtual Iterator_const& operator++() = 0;
			virtual const ANumRef& operator*() const = 0;
			virtual bool operator==(const Iterator_const&) const = 0;
			virtual bool operator!=(const Iterator_const&) const = 0;
		};
		virtual Iterator& begin() = 0;
		virtual Iterator_const& begin() const = 0;
		virtual Iterator& end() = 0;
		virtual Iterator_const& end() const = 0;
		virtual bool ordered() const
		{
			return true;
		}
		void copy(Iterator_const& src, Iterator& dst, Iterator& end)
		{
			for (; dst != end; ++dst, ++src)
				*dst = *src;
		}
        void fill(const ImageData& im)
        {
            Iterator_const& src = im.begin();
            Iterator& dst = this->begin();
            Iterator& end = this->end();
            for (; dst != end; ++dst, ++src)
				*dst = *src;
        }
        /// Write image to file
        virtual void write(const std::string &filename) const = 0;
        /// Get a clone of the image as a shared pointer
        virtual std::shared_ptr<ImageData> clone_as_sptr() const = 0;
	};
}

#endif