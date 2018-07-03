#include <QSerialPortInfo>
#include <QDebug>

int main()
{
    const auto infos = QSerialPortInfo::availablePorts();
    for (const QSerialPortInfo &info : infos)
    {
        qDebug() << info.portName();
        qDebug() << info.systemLocation();
        qDebug() << info.description();
        qDebug() << info.manufacturer();
        qDebug() << info.serialNumber();
        qDebug() << info.vendorIdentifier();
        qDebug() << info.productIdentifier();
        qDebug() << info.isBusy();
    }
    
    return EXIT_SUCCESS;
}
