namespace SupermarketSimulatorTool.Services;

public interface ICustomerService
{
    int TotalCustomers { get; }
    int ServedCustomers { get; }
    void SpawnCustomer();
    void ServeCustomer();
}