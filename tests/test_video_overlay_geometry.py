import unittest

from PySide6.QtCore import QSize

from py.video_geometry import (
    clamp_end_time,
    clamp_start_time,
    container_pct_to_video_pct,
    video_content_rect,
)


class VideoOverlayGeometryTests(unittest.TestCase):
    def test_wide_video_is_vertically_centered(self):
        rect = video_content_rect(QSize(730, 752), QSize(1920, 1080))

        self.assertEqual(rect.width(), 730)
        self.assertEqual(rect.height(), 410)
        self.assertEqual(rect.left(), 0)
        self.assertEqual(rect.top(), 171)

    def test_old_widget_percent_is_mapped_to_video_content(self):
        rect = video_content_rect(QSize(730, 752), QSize(1920, 1080))

        top = container_pct_to_video_pct(67.0, 752, rect)
        bottom = container_pct_to_video_pct(77.0, 752, rect)

        self.assertAlmostEqual(top, 81.18, places=2)
        self.assertAlmostEqual(bottom, 99.52, places=2)

    def test_matching_aspect_ratio_keeps_percent_unchanged(self):
        rect = video_content_rect(QSize(1280, 720), QSize(1920, 1080))

        self.assertEqual(rect.size(), QSize(1280, 720))
        self.assertAlmostEqual(
            container_pct_to_video_pct(80.0, 720, rect), 80.0
        )

    def test_start_time_stays_before_end_and_inside_timeline(self):
        self.assertEqual(clamp_start_time(80, 100, 120), 80)
        self.assertEqual(clamp_start_time(110, 100, 120), 99)
        self.assertEqual(clamp_start_time(-10, 100, 120), 0)

    def test_end_time_stays_after_start_and_inside_timeline(self):
        self.assertEqual(clamp_end_time(100, 80, 120), 100)
        self.assertEqual(clamp_end_time(50, 80, 120), 81)
        self.assertEqual(clamp_end_time(150, 80, 120), 120)

    def test_zero_duration_cannot_seek_outside_timeline(self):
        self.assertEqual(clamp_start_time(10, 20, 0), 0)
        self.assertEqual(clamp_end_time(10, 20, 0), 0)


if __name__ == "__main__":
    unittest.main()
