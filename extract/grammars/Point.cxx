#encoding "utf-8"

PointName -> AnyWord<wff=/[A-Z][0-9]*/>;

Point -> ("точка") PointName interp(Point.Name);
