#ifndef _ARRAYS_H
#define _ARRAYS_H


#ifdef WIN32
#if !defined(LIBMAL) && !defined(LIBATOMS) && !defined(LIBKERNEL) && !defined(LIBMAL) && !defined(LIBOPTIMIZER) && !defined(LIBSCHEDULER) && !defined(LIBMONETDB5)
#define algebra_export extern __declspec(dllimport)
#else
#define algebra_export extern __declspec(dllexport)
#endif
#else
#define algebra_export extern
#endif

algebra_export str ALGdimensionLeftfetchjoin1(bat* result, const bat* cands, const ptr *dims, const ptr *dim) ;
#if 0
algebra_export str ALGdimensionLeftfetchjoin2(bat* result, const ptr* dimsCand, const ptr *dims, const ptr *dim) ;
/* project a non-dimensional column based on oids selected over dimensions */
algebra_export str ALGnonDimensionLeftfetchjoin1(bat* result, const ptr* dimsCand, const bat *candBat, const bat *valsBat);
#endif
/* project a non-dimensional column based on oids selected over dimensions */
/*make sure that the BAT with the oids is an MBR and put NULL to values that are not in the oids but are needed to create the MBR*/
algebra_export str ALGnonDimensionLeftfetchjoin1(bat* result, const bat* cands, const bat *vals, const ptr *dims);
/* project a non-dimensional column based on tid (actually materialise it) */
algebra_export str ALGnonDimensionLeftfetchjoin2(bat* result, ptr* dimsRes, const bat *tids, const bat *vals, const ptr *dims);
//algebra_export str ALGnonDimensionLeftfetchjoin(bat *result, const bat *lid, const bat *rid);
//algebra_export str ALGdimensionLeftfetchjoin(bat *result, const bat *lid, const bat *rid);

algebra_export str ALGdimensionSubselect2(ptr *dimsRes, bat* oidsRes, const ptr *dims, const ptr* dim, const ptr *dimsCand, const bat* oidsCand,
                            const void *low, const void *high, const bit *li, const bit *hi, const bit *anti);
algebra_export str ALGdimensionSubselect1(ptr *dimsRes, bat* oidsRes, const ptr *dims, const ptr* dim, 
                            const void *low, const void *high, const bit *li, const bit *hi, const bit *anti);
algebra_export str ALGdimensionThetasubselect2(ptr *dimsRes, bat* oidsRes, const ptr *dims, const ptr* dim, const ptr *dimsCand, const bat* oidsCand, const void *val, const char **op);
algebra_export str ALGdimensionThetasubselect1(ptr *dimsRes, bat* oidsRes, const ptr *dims, const ptr* dim, const void *val, const char **op);


algebra_export str ALGnonDimensionSubselect2(ptr *dimsRes, bat* oidsRes, const ptr *dims, const bat* values, const ptr *dimsCand, const bat* oidsCand, 
                            const void *low, const void *high, const bit *li, const bit *hi, const bit *anti);
algebra_export str ALGnonDimensionSubselect1(ptr *dimsRes, bat* oidsRes, const ptr *dims, const bat* values, 
                            const void *low, const void *high, const bit *li, const bit *hi, const bit *anti);

algebra_export str ALGmbrsubselect(bat *result, const ptr *dims, const ptr* dim, const bat *sid, const bat *cid);
algebra_export str ALGmbrsubselect2(bat *result, const ptr *dims, const ptr* dim, const bat *sid);

algebra_export str ALGmbrproject(bat *result, const bat *bid, const bat *sid, const bat *rid);

algebra_export str ALGproject(bat *result, const ptr* candDims, const bat* candBAT);
#endif /* _ARRAYS_H */
