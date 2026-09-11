from PySide6.QtCore import QPoint, QRect, Qt


def video_content_rect(container_size, video_size):
    """Return the aspect-fitted video rect inside its display widget."""
    if (
        container_size.width() <= 0
        or container_size.height() <= 0
        or video_size.width() <= 0
        or video_size.height() <= 0
    ):
        return QRect(QPoint(0, 0), container_size)

    display_size = video_size.scaled(
        container_size, Qt.AspectRatioMode.KeepAspectRatio
    )
    x = (container_size.width() - display_size.width()) // 2
    y = (container_size.height() - display_size.height()) // 2
    return QRect(QPoint(x, y), display_size)


def container_pct_to_video_pct(percent, container_height, video_rect):
    """Convert an old full-widget vertical percentage to video coordinates."""
    if container_height <= 0 or video_rect.height() <= 0:
        return percent
    container_y = container_height * percent / 100.0
    video_y = container_y - video_rect.top()
    return max(0.0, min(100.0, video_y / video_rect.height() * 100.0))
