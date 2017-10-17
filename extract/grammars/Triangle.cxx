#encoding "utf-8"

PointNames -> AnyWord<wff=/([A-Z][0-9]*){3}/>;

Triangle -> "треугольник" PointNames interp(Triangle.Names);
