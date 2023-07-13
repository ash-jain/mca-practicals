/* 
 * Student Name - Aakash Jain.
 * Roll No. - 222010019.
 * Lab Experiment No. 6 - Refactor the following Java Code.
 */

import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import java.util.Scanner;


class NotificationVO {

    public Date date;
    public String message;

    public NotificationVO(Date date, String message) {
        this.date = date;
        this.message = message;
    }
}


abstract interface NotificationDAO {
    public UUID addNotification(Date time, String message);
    public NotificationVO getNotification(UUID id);
}


class MapNotificationDAO implements NotificationDAO {
    private final Map<UUID, NotificationVO> notifications = new HashMap<UUID, NotificationVO>();

    public UUID addNotification(Date time, String message) {
        UUID id = UUID.randomUUID();
        NotificationVO item = new NotificationVO(time, message);
        this.notifications.put(id, item);
        return id;
    }

    public NotificationVO getNotification(UUID id) {
        return this.notifications.get(id);
    }
}


class NotificationService {

    private MapNotificationDAO storage;

    NotificationService(MapNotificationDAO MNDao) {
        this.storage = MNDao;
    }

    public UUID raiseNotification(String message) {
        return this.storage.addNotification(new Date(), message);
    }

    public Date getNotificationTime(UUID id) {
        return this.storage.getNotification(id).date;
    }

    public String getNotificationMessage(UUID id) {
        return this.storage.getNotification(id).message;
    }

    public static void main(String[] args) {
        MapNotificationDAO MNDao = new MapNotificationDAO();
        NotificationService notificationService = new NotificationService(MNDao);

        int size = 0;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of notifications: ");
        size = sc.nextInt();
        sc.nextLine();
        String message;
        UUID[] refer = new UUID[size];

        for (int i = 0; i < size; i++) {
            System.out.print("Enter notification: ");
            message = sc.nextLine();
            refer[i] = notificationService.raiseNotification(message);
            System.out.println("Message saved!\n");
        }

        System.out.println("Notifications: ");

        for (int i = 0; i < size; i++) {
            System.out.println(notificationService.getNotificationTime(refer[i])+ " - " + notificationService.getNotificationMessage(refer[i]));
        }

    }
}
