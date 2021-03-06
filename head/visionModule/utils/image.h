#pragma once

//#define VISION_GRADIENT"
//#define VISION_EGB
#define VISION_CLUSTER

#include <list>
#include <map>
#include <string.h>
#include "jpeg.h"
#include <string>

#define NO_BORDER     0
#define BORDER_LEFT   1
#define BORDER_RIGHT  2
#define BORDER_TOP    4
#define BORDER_BOTTOM 8
#define BORDER_SKIP   16
#define FIRST_SEGMENT 32

struct TArea {
	int Start;
	int Size;
	int MinX;
	int MinY;
	int MaxX;
	int MaxY;
	char AtBorder;
        unsigned char ObjectType;

	TArea() {}

	TArea(const TArea& area) {
		Start = area.Start;
		Size = area.Size;
		MinX = area.MinX;
		MinY = area.MinY;
		MaxX = area.MaxX;
		MaxY = area.MaxY;
		AtBorder = area.AtBorder;
                ObjectType = area.ObjectType;
	}

	TArea(int x, int y) {
		Size = 1;
		MinX = x;
		MaxX = x;
		MinY = y;
		MaxY = y;
		AtBorder = 0;
                ObjectType = 0;
	}

	void Add(int x, int y) {
		if (x < MinX) {
			MinX = x;
		} else {
			if (x > MaxX) {
				MaxX = x;
			}
		}
		if (y < MinY) {
			MinY = y;
		} else {
			if (y > MaxY) {
				MaxY = y;
			}
		}
	}
};

template<class T>
class TMutableImage {

	bool Allocated;

protected:
	T* Image;

public:
	int Width;
	int Height;
	int Depth;

	TMutableImage() {
		Allocated = false;
	}

	TMutableImage(int width,
	              int height,
	              int depth) {
		Allocated = false;
		Allocate(width, height, depth);
	}

	TMutableImage(TMutableImage<T>* image, bool copy = true) {
		Allocated = false;
		Allocate(image->Width, image->Height, image->Depth);
		if (copy) {
			memcpy(Image, image->Image, ImageSize() * sizeof(T));
		}
	}

	TMutableImage(const char* dumpFileName) {
		Allocated = false;
		LoadDump(dumpFileName);
	}

	TMutableImage(T* src,
	              int width,
	              int height,
	              int depth) {
		Allocated = false;
		Width = width;
		Height = height;
		Depth = depth;
		Image = src;
	}

	TMutableImage(TMutableImage<T>* image,
	             int scale) {

		Allocated = false;
		Allocate(image->Width /scale, image->Height / scale, image->Depth);

		long sum[Depth];
		int n = scale * scale;
		for (int startX = 0; startX < Width; startX++) {
			for (int startY = 0; startY < Height; startY++) {
				//image->Average(x * scale, y * scale, scale, Cell(x, y));
				memset(sum, 0, Depth * sizeof(long));
				for (int x = 0; x < scale; x++) {
					for (int y = 0; y < scale; y++) {
						const T* p = image->Cell(startX * scale + x, startY * scale + y);
						for (int d = 0; d < Depth; d++) {
							sum[d] += p[d];
						}
					}
				}

				T* result = Cell(startX, startY);
				for (int d = 0; d < Depth; d++) {
					result[d] = sum[d] / n;
				}

			}
		}
	}

	~TMutableImage() {
		if (Allocated) {
			delete Image;
		}
	}

	T* Allocate() {
		if (Allocated) {
			delete Image;
		}
		Image = new T[ImageSize()];
		Allocated = true;
		return Image;
	}

	bool IsAllocated() {
		return Allocated;
	}

	void Allocate(int c) {
		Allocate();
		memset(Image, c, ImageSize());
	}

	void Allocate(int width, int height, int depth) {
		Width = width;
		Height = height;
		Depth = depth;
		Allocate();
	}

	bool ReAllocate(int width, int height, int depth) {
		if ((!Allocated) || (Width != width) || (Height != height) || (Depth != depth)) {
			Width = width;
			Height = height;
			Depth = depth;
			Allocate();
			return true;
		}
		return false;
	}

	void Allocate(int width, int height, int depth, int c) {
		Width = width;
		Height = height;
		Depth = depth;
		Allocate(c);
	}

	void Wrap(T* src) {
		if (Allocated) {
			delete Image;
			Allocated = false;
		}
		Image = src;
	}

	void CopyFrom(TMutableImage<T>* image) {
		if (!Allocated) {
			Width = image->Width;
			Height = image->Height;
			Depth = image->Depth;
			Allocate();
		}
		memcpy(Image, image->Image, ImageSize() * sizeof(T));
	}

	void LoadDump(const char* fileName) {
		FILE* file = fopen(fileName, "rb");
		if (file != NULL) {
			fread(&Width, 1, sizeof(int), file);
			fread(&Height, 1, sizeof(int), file);
			fread(&Depth, 1, sizeof(int), file);

			printf("LoadDump: %d x %d : %d\n", Width, Height, Depth);

			Allocate();
			fread(Image, sizeof(T), ImageSize(), file);
			fclose(file);
		} else {
			Width = 0;
			Height = 0;
			Depth = 0;
			Image = NULL;
		}
	}

	void SaveDump(const char* fileName) {
	    FILE *outfile = fopen( fileName, "wb");
	    if (outfile) {
	        fwrite(&Width, 1, sizeof(int), outfile);
	        fwrite(&Height, 1, sizeof(int), outfile);
	        fwrite(&Depth, 1, sizeof(int), outfile);
	        fwrite(Image, sizeof(T), ImageSize(), outfile);
	        fclose( outfile );
	    }
	}

	int Size() {
		return Width * Height;
	}

	int ImageSize() {
		return Width * Height * Depth;
	}

	int Idx(int x, int y) {
		return (y * Width + x);
	}

	T* Cell(int idx) {
		return Image + idx * Depth;
	}

	T* Cell(int x, int y) {
		return Cell(Idx(x, y));
	}

	void IdxToXY(int idx, int& x, int& y) {
		x = (idx / Depth) % Width;
		y = (idx / Depth) / Width;
	}

	TMutableImage<int>* a() { return NULL;}

	void DrawPointer(int x, int y, int size, T* color) {
		int maxX = x + size < Width ? x + size : Width;
		int maxY = y + size < Height ? y + size : Height;

		for (int i = x > size ? x - size : 0; i < maxX; i++) {
			for (int j = y > size ? y - size: 0; j < maxY; j++) {
				memcpy(Cell(i,j), color, Depth * sizeof(T));
			}
		}
	}

	void FillRect(int x, int y, int width, int height, T* color) {
		for (int i = 0; i < width; i++) {
			for (int j = 0; j < height; j++) {
				memcpy(Cell(x + i, y + j), color, Depth * sizeof(T));
			}
		}
	}

	void DrawHorizontal(int x, int y, int width, T* color) {
		if ((y < 0) || (y >= Height)) {
			return;
		}

		int right = x + width;
		if (right > Width) {
			right = Width;
		}

		if (x < 0) {
			x = 0;
		}

		for (int i = x; i < right; i++) {
			memcpy(Cell(i,y), color, Depth * sizeof(T));
		}
	}

	void DrawVertical(int x, int y, int height, T* color) {
		if ((x < 0) || (x >= Width)) {
			return;
		}

		int bottom = y + height;
		if (bottom > Height) {
			bottom = Height;
		}

		if (y < 0) {
			y = 0;
		}

		for (int i = y; i < bottom; i++) {
			memcpy(Cell(x,i), color, Depth * sizeof(T));
		}
	}

	void DrawRect(int x, int y, int width, int height, T* color) {
		DrawHorizontal(x, y, width, color);
		DrawHorizontal(x, y + height, width, color);
		DrawVertical(x, y, height, color);
		DrawVertical(x + width, y, height, color);
	}

	unsigned Diff(T* c1, T* c2) {
		unsigned diff = 0;
		for (int d = 0; d < Depth; d++) {
			int delta = c1[d] - (int)(c2[d]);
			diff += delta * delta;
		}
		return diff;
	}

	long GetDeviation(T* mean) {
		int size = Width * Height;
		unsigned long sum[Depth];
		memset(sum, 0, sizeof(sum));
		unsigned long sqxsum = 0;
		T* ptr = Image;
		for (int i = 0; i < size; i++) {
			for (int j = 0; j < Depth; j++) {
				long value = *ptr++;
				sum[j] += value;
				sqxsum += value * value;
			}
		}

		long meansq = 0;
		for (int j = 0; j < Depth; j++) {
			meansq += sum[j] * sum[j];
			mean[j] = (T)(sum[j] / size);
		}

		return (sqxsum - meansq / size) / size;
	}

	void SaveJpg(const char* filename) {
		write_jpeg_file(filename, Image, Width, Height, Depth);
	}
};

class TMutableRGBImage : public TMutableImage<unsigned char>, IWritableImage {

	int WritePtr;

public:
	//J_COLOR_SPACE ColorSpace;

	TMutableRGBImage(TMutableImage<unsigned char>* image, bool copy = true) :
		TMutableImage<unsigned char>(image, copy) {
		//ColorSpace = JCS_RGB;
	}

	TMutableRGBImage(const char* dumpFile) :
		TMutableImage(dumpFile) {
		//ColorSpace = JCS_RGB;
	}

	TMutableRGBImage() {}

	void ConvertToYUV();

	void SaveJpg(const char* filename) {
		write_jpeg_file(filename, Image, Width, Height, Depth);
	}

	void LoadJpg(const char* filename) {
		read_jpeg_file(filename, this);
	}

	virtual void SetDimensions(int width, int height, int depth) {
		//printf("SetDimensions: %d %d %d\n", width, height, depth);
		Allocate(width, height, depth);
		WritePtr = 0;
		//ColorSpace = JCS_RGB;
	}

	virtual void Write(const unsigned char* buffer, int size) {
		//printf("write: %d\n", size);
		memcpy(Image + WritePtr, buffer, size);
		WritePtr += size;
		//printf("write: OK %d\n", WritePtr);
	}
};

typedef unsigned char* TSamplerCell;

class TSegmentsExtractor {
public:
	virtual void ExtractSegments(std::list<TArea>& area) {}
	virtual void DrawDebugInfo(TMutableRGBImage* image) {}

	virtual ~TSegmentsExtractor(){}
};

struct TValidationResult {
	double LikelyBackground;
	double LikelyObject;
};

enum AreaType {
	LIKELY_FALSE_DETECTION = 1,
	LIKELY_OBJECT = 2,
	LIKELY_BACKGROUD = 3,
	LIKELY_INCOMPLETED_BACKGROUND = 4
};

class TObjectValidator {

	double ImageWidth;
	double ImageHeight;

public:

	double MinBackgroundAreaPct;
	double MinObjectAreaPct;
	double MaxObjectAreaPct;

	TObjectValidator() {
		MinBackgroundAreaPct = 0.4;
		MinObjectAreaPct = 0.01;
		MaxObjectAreaPct = 0.5;
	}

	void SetImageSize(int width, int height) {
		ImageWidth = width;
		ImageHeight = height;
	}

	void ValidateBackgroundBySize(unsigned areaSize, int border, TValidationResult& result);
	int ValidateArea(TArea* area);
	AreaType ClassifyArea(TArea* area);
};

class TExtractorFactory {

public:

	std::map<std::string,int*> IntParameters;
	std::map<std::string,double*> DoubleParameters;

	virtual TSegmentsExtractor* CreateExtractor(TMutableImage<unsigned char>* image) = 0;

	void AddParameter(const char* name, int* ptr) {
		std::string str(name);
		IntParameters[str] = ptr;
	}

	void AddParameter(const char* name, double* ptr) {
		std::string str(name);
		DoubleParameters[str] = ptr;
	}

	void AddParameter(const char* name, int* ptr, int value) {
		AddParameter(name, ptr);
		*ptr = value;
	}

	void AddParameter(const char* name, double* ptr, double value) {
		AddParameter(name, ptr);
		*ptr = value;
	}

	bool Set(const char* name, int value) {
		std::string str(name);
		std::map<std::string,int*>::iterator it = IntParameters.find(str);
		if (it != IntParameters.end()) {
			*(it->second) = value;
			return true;
		} else {
			return false;
		}
	}

	bool Set(const char* name, double value) {
		std::string str(name);
		std::map<std::string,double*>::iterator it = DoubleParameters.find(str);
		if (it != DoubleParameters.end()) {
			*(it->second) = value;
			return true;
		} else {
			return false;
		}
	}

	bool Get(const char* name, int* value) {
		std::string str(name);
		std::map<std::string,int*>::iterator it = IntParameters.find(str);
		if (it != IntParameters.end()) {
			*value = *(it->second);
			return true;
		} else {
			return false;
		}
	}

	bool Get(const char* name, double* value) {
		std::string str(name);
		std::map<std::string,double*>::iterator it = DoubleParameters.find(str);
		if (it != DoubleParameters.end()) {
			*value = *(it->second);
			return true;
		} else {
			return false;
		}
	}
};

void ReverseMatrix(int n, double* matrix, double* inv);
void MakeRegressionMatrix(TMutableImage<double>* regressionMatrix);
