#encoding "utf-8"

PointName -> AnyWord<wff=/[A-Z]/>;

Point -> "точка" PointName interp(Point.Name);
