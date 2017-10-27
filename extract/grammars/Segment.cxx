#encoding "utf-8"

PointNames -> AnyWord<wff=/([A-Z][0-9]*){2}/>;
NumberString -> AnyWord<wff=/[0-9]*((\.|,)[0-9]+)?/>;

SegmentBase -> PointNames interp(Segment.EndPoints);

Segment -> Noun<kwtype="отрезок_название"> SegmentBase+;
Segment -> PointNames interp(Segment.Names) AnyWord<kwtype="равно"> NumberString interp(Segment.Length);